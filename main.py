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
client = mqtt.Client()
client.connect("205.236.77.2", 1883, 60)

# read data using pin 14
while True:
    client.loop_forever()
    try:
        time.sleep(1.0)

        result = instance.read()
        if result.is_valid():
            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)
        else:
            print("Error: %d" % result.error_code)

    except:
        print("Error: %d" % result.error_code)
