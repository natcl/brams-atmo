#!/usr/bin/python
import os
import subprocess
import time
import json

with open('config.json', 'r') as config:
    config_data = json.loads(config.read())

while True:
    p = subprocess.Popen('/home/pi/brams-atmo/bin/loldht', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, error = p.communicate()
    for line in out.split('\n'):
        if line.startswith('Humidity'):
            humidity = line[11:16]
            temperature = line[33:38]
            with open('TEMP', 'w') as t:
                t.write(temperature)
            with open('HUMIDITY','w') as h:
                h.write(humidity)
            print(temperature + ' ' + humidity)

    time.sleep(config_data['poll_interval'])
