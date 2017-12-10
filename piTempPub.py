#!/usr/bin/python3.5
import paho.mqtt.client as mqtt
import time
import os


# Onboard raspberry pi temperature measurement
def measure_temp():
    temp = os.popen("vcgencmd measure_temp").readline()
    # looks like temp=25.48'C\n
    # Only want to publish the value
    # some search and replace to get only the info I want
    temp1 = temp.replace("temp=", "")
    return (temp1.replace("\n", ""))

# running on same computer as Mosquitto so using localhost
brokerAddress = "localhost"  # "192.168.1.247"
client = mqtt.Client("piTempMon")# read with Jamaican accent
client.connect(brokerAddress)

while True:
    time.sleep(5)
    theTemp = measure_temp()
    # and is finally published here
    client.publish("pi_temp", theTemp)
