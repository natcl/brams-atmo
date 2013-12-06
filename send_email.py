#!/usr/bin/python

import json
import smtplib

with open('config.json', 'r') as config:
    config_data = json.loads(config.read())

if config_data['email_notifications']:
    sender = config_data['email_from']
    receivers = config_data['email_to']

    message = "From: {1} <{0}>\nTo: {1} <{0}>\nSubject: {1} alert\nPlease check {1}, temperature problem".format(config_data['email_from'], config_data['name'])

    try:
       smtpObj = smtplib.SMTP('smtp.umontreal.ca')
       smtpObj.sendmail(sender, receivers, message)         
       print "Successfully sent email"
    except:
       print "Error: unable to send email"
else:
    print('Email notifications off')
