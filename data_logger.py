import time
import socket
#from adaLCD import adaLCD
from sparkfunLCD import sparkfunLCD as adaLCD
import logging
from logging.handlers import TimedRotatingFileHandler
from sht1x.Sht1x import Sht1x as SHT1x

dataPin = 11
clkPin = 7
sht1x = SHT1x(dataPin, clkPin, SHT1x.GPIO_BOARD)

lcd = adaLCD('/dev/ttyAMA0')

hostname = socket.gethostname()

logHandler = TimedRotatingFileHandler("/var/log/{0}.log".format(hostname),when="H", interval=1)
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
        temperature = sht1x.read_temperature_C()
        humidity = sht1x.read_humidity()
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
