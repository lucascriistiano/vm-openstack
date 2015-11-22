# host = "10.9.98.162"
host = "127.0.0.1"
port = 1883
qos = 1

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