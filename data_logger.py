import time
import logging
from logging.handlers import TimedRotatingFileHandler
from adaLCD import adaLCD
from sht1x.Sht1x import Sht1x as SHT1x

dataPin = 11
clkPin = 7
sht1x = SHT1x(dataPin, clkPin, SHT1x.GPIO_BOARD)

logHandler = TimedRotatingFileHandler("atmo-piano.log",when="M", interval=2)
logFormatter = logging.Formatter('%(asctime)s %(message)s')
logHandler.setFormatter( logFormatter )
logger = logging.getLogger( 'AtmoPiano' )
logger.addHandler( logHandler )
logger.setLevel( logging.INFO )

lcd = adaLCD('/dev/ttyACM0')
lcd.clear()
lcd.backlight_on()
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
        lcd.write('\n\r')
        lcd.write('Humidity: {0:.2f}'.format(humidity))
        logger.info('T: {0:.2f} H: {1:.2f}'.format(temperature,humidity))
        time.sleep(2)

except KeyboardInterrupt:
    print('Shutting down')
    lcd.clear()
    lcd.backlight_off()
    lcd.close()
