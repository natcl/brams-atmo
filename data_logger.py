#!/usr/bin/python

import json
import time
import socket
import logging
from logging.handlers import TimedRotatingFileHandler

with open('config.json', 'r') as config:
    config_data = json.loads(config.read())

# Will log every 5 minutes with a file rollover on Mondays

logHandler = TimedRotatingFileHandler("/var/log/atmo.log", when="W0")
logFormatter = logging.Formatter('%(asctime)s %(message)s')
logHandler.setFormatter(logFormatter)
logger = logging.getLogger(config_data['name'])
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)

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
        logger.info('T: {0:.2f} H: {1:.2f}'.format(temperature,humidity))
        time.sleep(60*5)

except KeyboardInterrupt:
    print('Shutting down')
