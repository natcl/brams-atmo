import time
import socket
#from adaLCD import adaLCD
from sparkfunLCD import sparkfunLCD as adaLCD
import logging
from logging.handlers import TimedRotatingFileHandler
import urllib2
import json

lcd = adaLCD('/dev/ttyAMA0')

hostname = socket.gethostname()

logHandler = TimedRotatingFileHandler("/var/log/{0}.log".format(hostname),when="D", interval=1)
logFormatter = logging.Formatter('%(asctime)s %(message)s')
logHandler.setFormatter(logFormatter)
logger = logging.getLogger(hostname)
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)

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
        logger.info('T: {0:.2f} H: {1:.2f}'.format(temperature,humidity))
        time.sleep(60)

except KeyboardInterrupt:
    print('Shutting down')
    lcd.clear()
    lcd.close()
