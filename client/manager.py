import serial
import time
import threading
import config

class SerialManager(threading.Thread):
    """Reads and writes values to serial and manages interesteds in listen serial"""

    def __init__(self, mqtt_manager, serial_port, baud_rate = 9600, timeout = 3):
        super(SerialManager, self).__init__()
        self.mqtt_manager = mqtt_manager
        self.mqtt_manager.subscribe(self)

        # self.interesteds = []  # Create a list of interesteds
        self.serial = serial.Serial(serial_port, baud_rate, timeout=timeout)

    def run(self):
        while True:
            line = self.serial.readline()

            if len(line) > 0:
                line = line[:-1]
                items = line.split(",")

                device_code = int(items[0])
                value = int(items[1])

                if device_code == config.ntc_code:
                    self.mqtt_manager.publish_value(config.ntc_topic, value)
                elif device_code == config.ldr_code:
                    self.mqtt_manager.publish_value(config.ldr_topic, value)
                elif device_code == config.auth_code:
                    self.mqtt_manager.publish_value(config.auth_topic, value)
                elif device_code == config.pir_code:
                    self.mqtt_manager.publish_value(config.pir_topic, value)

    def notify(self, topic, message):
        value = int(message)
        value_chr = chr(value)

        if topic == config.fan_topic:
            line = chr(config.fan_code) + chr(config.fan_change_speed) + value_chr
            self.write(line)
        elif topic == config.gate_topic:
            line = chr(config.gate_code) + value_chr
            self.write(line)
        elif topic == config.light_topic:
            line = chr(config.light_code) + value_chr
            self.write(line)

    def __wait_for_data(self, serial, bytes_size, max_time):
        initial_time = time.time()
        elapsed_time = 0

        while(elapsed_time < max_time and serial.inWaiting() < bytes_size):
            elapsed_time = time.time() - initial_time
            pass

        print serial.inWaiting()
        return (serial.inWaiting() == bytes_size)

    # def subscribe(self, interested):
    #     self.interesteds.append(interested)

    # def unsubscribe(self, interested):
    #     self.interesteds.remove(interested)

    # def read(self, bytes):
    #     return self.read_from(self.serial, bytes)

    def write(self, line):
        self.write_on(self.serial, line)

    # def read_from(self, ser, bytes):
    #     line = ''
    #     line_values = ''
    #     print '[SERIAL_MANAGER] reading line'

    #     for x in xrange(0,bytes):
    #         reading = ser.read()

    #         if(len(reading) > 0):
    #             line += reading
    #             line_values += str(ord(reading))

    #             if(x < bytes - 1):
    #                 line_values += ' '

    #     print '[SERIAL_MANAGER] received <%s>' % line_values
    #     return line

    def write_on(self, ser, line):
        line_values = ''
        for x in xrange(0,len(line)):
            line_values += str(ord(line[x]))

            if(x < len(line) - 1):
                line_values += ' '

        print '[SERIAL_MANAGER] sending <%s>' % line_values
        ser.write(line)

    # def respond(self, byte):
    #     self.write(chr(byte))

    # def execute(self, byte, operation):
    #     self.write("%s%s" % (chr(byte), chr(operation)))
    #     return self.read(2)

    # def execute_reading(self, byte):
    #     self.write(chr(byte))
    #     return self.read(3)

    # def execute_with_param(self, byte, operation, param):
    #     self.write("%s%s%s" % (chr(byte), chr(operation), chr(param)))
    #     return self.read(2)