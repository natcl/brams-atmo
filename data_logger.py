import time
from adaLCD import adaLCD
from sht1x.Sht1x import Sht1x as SHT1x

dataPin = 11
clkPin = 7
sht1x = SHT1x(dataPin, clkPin, SHT1x.GPIO_BOARD)

lcd = adaLCD('/dev/ttyACM0')
lcd.clear()
lcd.backlight_on()

try:
    while(True):
        lcd.clear()
        temperature = sht1x.read_temperature_C()
        humidity = sht1x.read_humidity()
        lcd.print(temperature)
        lcd.print(humidity)
        time.sleep(2)
except:
    print('Shutting down')
    lcd.close()
