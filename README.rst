**************
IOT-Adventures
**************
My (mis)-adventures in the World of IOT including ESP32, ESP8266, Raspberry Pi, and Arduino.

First Project
#############
MQTT between ESP8266 and Raspberry Pi

Hardware
	ESP8266 `(Adafruit Feather Huzzah) <https://www.adafruit.com/product/2821>`_ using micropython mqtt client. `With Feather Wing OLED <https://www.adafruit.com/product/2900>`_

	Raspberry Pi (any will do with a network connection)

Software
	Raspberry Pi
		Mosiquitto for Raspberry Pi + custom python script for  MQTT client publishing RPI temperature. 
	ESP8266
		Custom micropython script.
		Imports
			network
			machine
			ssd1306
			time
			simple.MQTTClient
.. code-block:: python

    print("hello World")