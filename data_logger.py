#!/usr/bin/python

import json
import time
import socket
import logging
from logging.handlers import TimedRotatingFileHandler
import urllib2

with open('config.json', 'r') as config:
    config_data = json.loads(config.read())

# Will log every 5 minutes with a file rollover on Mondays

logHandler = TimedRotatingFileHandler("/var/log/{0}.log".format(config_data['name']), when="W0")
logFormatter = logging.Formatter('%(asctime)s %(message)s')
logHandler.setFormatter(logFormatter)
logger = logging.getLogger(config_data['name'])
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)

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
        logger.info('T: {0:.2f} H: {1:.2f}'.format(temperature,humidity))
        time.sleep(60*5)

except KeyboardInterrupt:
    print('Shutting down')
