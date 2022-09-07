import time

import RPi.GPIO as GPIO
import dht11

# initialize GPIO
from paho import mqtt
import paho.mqtt.client as mqtt

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
instance = dht11.DHT11(pin = 27)
# read data using pin 14

broker_url = "10.4.1.212"
broker_port = 1883

client = mqtt.Client()
client.connect(broker_url, broker_port)


def on_connect(client, userdata, flags, rc):
   print("Connected With Result Code: {}".format(rc))

def on_disconnect(client, userdata, rc):
   print("Client Got Disconnected")

while True:

    try:

        time.sleep(1.0)

        result = instance.read()

        client.loop()
        if result.is_valid():
            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)
            client.publish(topic="TestingTopic", payload="Temperature: %-3.1f C" % result.temperature, qos=1, retain=False)
        else:
            print("Error: %d" % result.error_code)


    except:
        print("Error: %d" % result.error_code)
