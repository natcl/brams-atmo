#!/usr/bin/python

import dhtreader
import time

dhtPin = 4
dhtreader.init()

temperature = None
humidity = None

while True:
    try:
        temperature, humidity = dhtreader.read(22, dhtPin)
    except:
        print('Error reading sensor')
    
    if isinstance(temperature, float) and isinstance(humidity, float):
        with open('TEMP', 'w') as t:
            t.write('{0:.2f}'.format(temperature))
        with open('HUMIDITY','w') as h:
            h.write('{0:.2f}'.format(humidity))
    	print(str(temperature) + " " + str(humidity))
    time.sleep(3)
