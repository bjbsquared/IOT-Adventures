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
		Mosiquitto for Raspberry Pi + custom python script for  Paho MQTT client publishing RPI temperature. 
	ESP8266
		Custom micropython script.

		Imports
			* network
			* machine
			* ssd1306
			* time
			* simple.
			

Online References
	`Ampy <https://github.com/adafruit/ampy>`_
	`Espressif esptool <https://github.com/espressif/esptool>`_
	`micropython docs <http://docs.micropython.org/en/latest/pyboard/>`_
	`Screen for MAC or PuTTY for Windows <https://learn.adafruit.com/micropython-basics-how-to-load-micropython-on-a-board/>`_
	`Raspberry Pi ESP32 MicroPython MQTT DHT22 Tutorial <https://www.rototron.info/raspberry-pi-esp32-micropython-mqtt-dht22-tutorial/>`_
	`adafruit feather OLED guide <https://learn.adafruit.com/micropython-hardware-ssd1306-oled-display>`_


	








