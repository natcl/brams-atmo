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
    
    if temperature is not None and humidity is not None:
        with open('TEMP', 'w') as t:
            t.write(str(temperature))
        with open('HUMIDITY','w') as h:
            h.write(str(humidity))
        print(str(temperature) + " " + str(humidity))
    time.sleep(3)
