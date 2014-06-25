#!/usr/bin/python
import os
import subprocess
import time
import json

with open('config.json', 'r') as config:
    config_data = json.loads(config.read())

if config_data['dht_driver'] == 'adafruit':
    import Adafruit_DHT
    sensor = Adafruit_DHT.DHT22
    pin = 4

def update_lol():
    p = subprocess.Popen('/home/pi/brams-atmo/bin/loldht', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, error = p.communicate()
    for line in out.split('\n'):
        if line.startswith('Humidity'):
            humidity = line[11:16]
            temperature = line[33:38]

            return (temperature, humidity)
    return False

def update_adafruit():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        return ( '{:.2f}'.format(temperature), '{:.2f}'.format(humidity) )
    else:
        return False

def commit_to_file(temperature, humidity):
    with open('TEMP', 'w') as t:
        t.write(temperature)
    
    with open('HUMIDITY','w') as h:
        h.write(humidity)
    
    print(temperature + ' ' + humidity)

while True:
    if config_data['dht_driver'] == 'adafruit':
        result = update_adafruit()
    
    if config_data['dht_driver'] == 'lol':
        result = update_lol()
    
    if result is not False:
        commit_to_file(*result)
    else:
        print('Bad result, aborting')
  
    time.sleep(config_data['poll_interval'])
