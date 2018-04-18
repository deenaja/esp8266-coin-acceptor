from umqtt.simple import MQTTClient
import ubinascii
import machine

SERVER = "deenaja.com"
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
TOPIC = b"coin"


def pub(message="1"):
    global SERVER
    c = MQTTClient(CLIENT_ID, SERVER)
    c.connect()
    print("Connected to %s, waiting for button presses" % SERVER)
    c.publish(TOPIC, message.encode())
    c.disconnect()