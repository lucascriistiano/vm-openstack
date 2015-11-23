import threading
import config
import paho.mqtt.client as mqtt

class MqttManager(threading.Thread):
    """Manages Mqtt connection to updates and listening"""

    interesteds = []  # Create a list of interesteds

    def __init__(self, host, port, username = None, password = None):
        super(MqttManager, self).__init__()

        self.client = mqtt.Client()
        self.client.on_connect = self.__on_connect__
        self.client.on_message = self.__on_message__
        # self.client.username_pw_set(username, password)
        self.client.connect(host, port, 60)

    @staticmethod
    def __on_connect__(client, userdata, rc):
        print '[MQTT_MANAGER] Connected with result code %s' % str(rc)
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        subs = config.actuators_topic + "/#"
        client.subscribe(subs)
        print '[MQTT_MANAGER] Subscribed to %s' % subs

    @staticmethod
    def __on_message__(client, userdata, msg):
        topic = str(msg.topic)
        message = str(msg.payload)
        print '[MQTT_MANAGER] Received %s %s' % (topic, message)

        # notify interesteds with the message
        for interested in MqttManager.interesteds:
            interested.notify(topic, message)

    def subscribe(self, interested):
        MqttManager.interesteds.append(interested)

    def unsubscribe(self, interested):
        MqttManager.interesteds.remove(interested)

    def publish_value(self, topic, payload):
        self.client.publish(topic, payload)
        print '[MQTT_MANAGER] Sent %s %s' % (topic, payload)

    def run(self):
        print '[MQTT_MANAGER] Listening'
        self.client.loop_forever()

    def stop(self):
        self.client.disconnect()
        print '[MQTT_MANAGER] Stopped'