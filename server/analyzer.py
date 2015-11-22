import config

class SensorAnalyzer(object):
    """docstring for SensorAnalyzer"""

    temperature_limit_speed_0 = 25
    temperature_limit_speed_1 = 27
    temperature_limit_speed_2 = 30
    luminosity_limit          = 100
    allowed_access            = "22699470174"

    def __init__(self, mqtt_manager):
        super(SensorAnalyzer, self).__init__()

        self.mqtt_manager = mqtt_manager
        self.mqtt_manager.subscribe(self)

        self.presence = False
        self.temperature = 0
        self.luminosity = 0
        self.auth = ""

        self.fan_speed = 0
        self.light_bright = 0
        self.gate_state = 0

    def notify(self, topic, message):
        if topic == config.ldr_topic:
            self.luminosity = int(message)

        elif topic == config.pir_topic:
            pir_value = int(message)
            self.presence = (pir_value == 1)

        elif topic == config.ntc_topic:
            ntc_value = int(message)
            self.temperature = ntc_value

        elif topic == config.auth_topic:
            self.auth = message

        self.check_changes()

    def check_changes(self):
        if not self.presence:
            self.fan_speed = 0
            self.light_bright = 0
            self.gate_state = 0
        else:
            # Analyze temperature
            if self.temperature > SensorAnalyzer.temperature_limit_speed_2:
                self.fan_speed = 3
            elif self.temperature > SensorAnalyzer.temperature_limit_speed_2:
                self.fan_speed = 2
            elif self.temperature > SensorAnalyzer.temperature_limit_speed_0:
                self.fan_speed = 1
            else:
                self.fanSpeed = 0

            # Analyze luminosity
            if self.luminosity > SensorAnalyzer.luminosity_limit:
                self.light_bright = 0
            else:
                self.light_bright = 255

            # Analyze auth
            if self.auth == SensorAnalyzer.allowed_access:
                self.gate_state = 1
            else:
                self.gate_state = 0

        self.send_current_state()

    def send_current_state(self):
        self.mqtt_manager.publish_value(config.fan_topic, str(self.fan_speed))
        self.mqtt_manager.publish_value(config.light_topic, str(self.light_bright))
        self.mqtt_manager.publish_value(config.gate_topic, str(self.gate_state))