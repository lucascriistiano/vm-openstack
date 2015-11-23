# SERIAL CONFIG
serial = {}
serial['port']     = "/dev/tty.usbmodem1421"  # For Mac OSX
serial['baudrate'] = 9600
serial['timeout']  = 3

# MQTT CONFIG
host = "10.9.98.162"
# host = "127.0.0.1"
port = 1883
qos = 1

# DEVICES CODES
# SENSORS
ntc_code  = 1
ldr_code  = 2
auth_code = 3
pir_code  = 4
# ACTUATORS
light_code = 5
fan_code   = 6
gate_code  = 7

# FAN SPEEDS
fan_speeds = [ 0, 64, 128, 255 ]

# FAN OPERATIONS
fan_turn_on      = 1
fan_turn_off     = 2
fan_change_speed = 3

# GATE OPERATIONS
gate_open  = 1
gate_close = 2

# LIGHT OPERATIONS
light_turn_off      = 1
light_turn_on       = 2
light_change_bright = 3

# PREFERENCES
temperature_limit_speed_0 = 25
temperature_limit_speed_1 = 27
temperature_limit_speed_2 = 30
luminosity_limit          = 100
allowed_access            = "22699470174"

# DEVICES TOPICS
topic_prefix = "smarthouse";

sensors_topic   = topic_prefix + "/sensors";
actuators_topic = topic_prefix + "/actuators";

ldr_topic  = sensors_topic + "/ldr";
ntc_topic  = sensors_topic + "/ntc";
pir_topic  = sensors_topic + "/pir";
auth_topic = sensors_topic + "/auth";

fan_topic   = actuators_topic + "/fan";
gate_topic  = actuators_topic + "/gate";
light_topic = actuators_topic + "/light";