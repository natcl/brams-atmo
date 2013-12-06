#!/usr/bin/python

import json
import time
import urllib2

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
    while(True):
        json_data = None
        while(json_data is None):
            try:
                json_data = json.loads(urllib2.urlopen('http://localhost:8080/json').read()) 
                temperature = json_data[u'temperature']
                humidity = json_data[u'humidity']
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
        time.sleep(2)

except KeyboardInterrupt:
    print('Shutting down')
    lcd.clear()
    lcd.close()
