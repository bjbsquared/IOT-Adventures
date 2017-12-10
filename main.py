# MQTT trial program
# connects to the internal network
# sets up an OLED screen
# connects and subscribes to MQTT Broker and messages
import network
import machine
import ssd1306
import time
from simple import MQTTClient


SERVER = '192.168.1.247'  # Raspberry Pi running MQTT Broker
CLIENT_ID = 'ESP8266_OLED'  # Client name
TOPIC = b'pi_temp'  # Topic to listen for

# Connect to network
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect("SSID", "passWord")
time.sleep(1)

while not station.isconnected():
    time.sleep_ms(50)

print("Connection successful")
print(station.ifconfig())

# Setup for feather OLED Shield
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
oled = ssd1306.SSD1306_I2C(128, 32, i2c)

oled.text('Hello', 0, 0)
oled.text(station.ifconfig(), 0, 20)
oled.show()


blinkLine = 0  # variable toggles to blink something on the display

# Publish test messages e.g. with:
# mosquitto_pub -t pi_temp -m 54

# Received messages from subscriptions will be delivered to this callback


def sub_callback(topic, msg):
    global blinkLine

    oled.fill(0)
    oled.text(topic, 0, 0)
    oled.text(station.ifconfig(), 0, 20)

    if (blinkLine == 1):
        oled.text(msg, 0, 10)
    else:
        oled.text(msg + b'   *', 0, 10)
    oled.show()
    blinkLine = 1 - blinkLine


time.sleep(10)  # wakeup time is needed?
c = MQTTClient(CLIENT_ID, SERVER)
c.set_callback(sub_callback)

#Not sure why I had some issues connecting sometimes

while 1:
    try:
        c.connect()
    except OSError as e:
        print("mqtt: %r" % e)
        time.sleep(1)
    else:
        print("mqtt connected")
        break

c.subscribe(TOPIC)
while True:
    #used a switch for experimnetation
    if False:
        # Blocking wait for message
        c.wait_msg()
    else:
        # Non-blocking wait for message
        resp = c.check_msg()
        # Then need to sleep to avoid 100% CPU usage (in a real
        # app other useful actions would be performed instead)
        time.sleep(1)


c.disconnect()
