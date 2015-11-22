from manager import MqttManager
from analyzer import SensorAnalyzer
import config

def main():
    mqtt_manager = MqttManager(config.host, config.port)
    analyzer = SensorAnalyzer(mqtt_manager)

    mqtt_manager.start()

if __name__ == '__main__':
    main()