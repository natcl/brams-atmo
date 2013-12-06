#!/usr/bin/python

import json
import smtplib
import time
import urllib2
import datetime



sent_flag = False
sent_day = 0

def send_mail(temperature, humidity):
    sender = config_data['email_from']
    receivers = config_data['email_to']

    message = "From: {1} <{0}>\nTo: {1} <{0}>\nSubject: {1} alert\nPlease check {1}, temperature : {2}C, humidity : {3}%".format(config_data['email_from'], config_data['name'], temperature, humidity)

    try:
       smtpObj = smtplib.SMTP('smtp.umontreal.ca')
       smtpObj.sendmail(sender, receivers, message)         
       print "Successfully sent email"
    except:
       print "Error: unable to send email"

while True:
    
    with open('config.json', 'r') as config:
        config_data = json.loads(config.read())
    
    if config_data['email_notifications']:
        if datetime.datetime.now().day > sent_day:
            sent_flag = False
        json_data = None
        while json_data is None:
            try:
                json_data = json.loads(urllib2.urlopen('http://localhost:8080/json').read()) 
                temperature = json_data[u'temperature']
                humidity = json_data[u'humidity']
            except:
                pass
        if humidity < config_data['humidity_low'] or humidity > config_data['humidity_high'] or temperature < config_data['temperature_low'] or temperature > config_data['temperature_high']:
            if not sent_flag:
                send_mail(temperature, humidity)
                sent_flag = True
                sent_day = datetime.datetime.now().day

    time.sleep(30)