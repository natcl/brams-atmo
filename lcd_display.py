#!/usr/bin/python

import json
import time

with open('config.json', 'r') as config:
    config_data = json.loads(config.read())

if config_data['lcd_driver'] == 'sparkfun':
    from sparkfunLCD import sparkfunLCD as LCD
if config_data['lcd_driver'] == 'adafruit':
    from adaLCD import adaLCD as LCD

lcd = LCD('/dev/ttyAMA0')

lcd.clear()
lcd.contrast(220)
lcd.brightness(255)
lcd.rgb(0,255,0)

try:
    while True:
        temperature, humidity = (None, None)
        while (temperature is None and humidity is None):
            try:
                with open('TEMP', 'r') as t:
                    temperature = float(t.read())
                with open('HUMIDITY', 'r') as h:
                    humidity = float(h.read())
            except:
                pass

        if humidity > 60:
            lcd.rgb(255,0,0)
        else:
            lcd.rgb(0,255,0)
        lcd.clear()
        lcd.write('Temp:     {0:.2f}'.format(temperature))
        lcd.linefeed()
        lcd.write('Humidity: {0:.2f}'.format(humidity))
        time.sleep(10)

except KeyboardInterrupt:
    print('Shutting down')
    lcd.clear()
    lcd.close()
