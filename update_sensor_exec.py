#!/usr/bin/python
import os
import time
import json

with open('config.json', 'r') as config:
    config_data = json.loads(config.read())

while True:
    os.system('/home/pi/brams-atmo/update_sensor_once.py')
    time.sleep(config_data['poll_interval'])
