import config

class SensorAnalyzer(object):
    """docstring for SensorAnalyzer"""

    def __init__(self, mqtt_manager):
        super(SensorAnalyzer, self).__init__()

        self.mqtt_manager = mqtt_manager
        self.mqtt_manager.subscribe(self)

        self.presence = False
        self.temperature = 0
        self.luminosity = 0
        self.auth = ""

        self.fan_speed = 0
        self.light_state = 0
        self.gate_state = 0

    def notify(self, topic, message):
        if topic == config.ldr_topic:
            self.luminosity = int(message)

            if self.presence:
               self.analyze_luminosity()

        elif topic == config.pir_topic:
            pir_value = int(message)
            self.presence = (pir_value == 1)

            if self.presence:
                self.analyze_temperature()
                self.analyze_luminosity()
            else:
                self.mqtt_manager.publish_value(config.light_topic, str(config.light_turn_off))
                self.mqtt_manager.publish_value(config.fan_topic, str(config.fan_speeds[0]))

        elif topic == config.ntc_topic:
            ntc_value = int(message)
            self.temperature = ntc_value

            if self.presence:
                self.analyze_temperature()

        elif topic == config.auth_topic:
            self.auth = message
            self.analyze_auth()


    def analyze_luminosity(self):
         # Analyze luminosity
        if self.luminosity > config.luminosity_limit:
            self.mqtt_manager.publish_value(config.light_topic, str(config.light_turn_off))
        else:
            self.mqtt_manager.publish_value(config.light_topic, str(config.light_turn_on))

    def analyze_temperature(self):
        # Analyze temperature
        if self.temperature > config.temperature_limit_speed_2:
            self.fan_speed = 3
        elif self.temperature > config.temperature_limit_speed_2:
            self.fan_speed = 2
        elif self.temperature > config.temperature_limit_speed_0:
            self.fan_speed = 1
        else:
            self.fanSpeed = 0

        self.mqtt_manager.publish_value(config.fan_topic, str(config.fan_speeds[self.fan_speed]))

    def analyze_auth(self):
        # Analyze auth
        if self.auth == config.allowed_access:
            self.mqtt_manager.publish_value(config.gate_topic, str(config.gate_open))
        else:
            self.mqtt_manager.publish_value(config.gate_topic, str(config.gate_close))

