from mqtt import MqttManager
from manager import SerialManager
import config

def main():
    mqtt_manager = MqttManager(config.host, config.port)
    serial_manager = SerialManager(mqtt_manager, config.serial['port'], config.serial['baudrate'], config.serial['timeout'])

    mqtt_manager.start()
    serial_manager.start()

if __name__ == '__main__':
    main()