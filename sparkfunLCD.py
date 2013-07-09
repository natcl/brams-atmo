#!/usr/bin/python
import serial

BACKLIGHT_ON = chr(0x80) + chr(255 )
BACKLIGHT_OFF = chr(0x80) + chr(0)
BRIGHTNESS = chr(0x80) + '{0}'
CLEAR = chr(0xFE) + chr(0x01)

class sparkfunLCD(object):
    def __init__(self, port):
        self.lcd = serial.Serial(port, 9600)

        self._brightness = 0
    
    def clear(self):
        self.lcd.write(CLEAR)
    
    def home(self):
        pass

    def backlight_on(self):
        self.lcd.write(BACKLIGHT_ON)

    def backlight_off(self):
        self.lcd.write(BACKLIGHT_OFF)

    def brightness(self, value):
        if self._brightness == value:
            return
        else:
            self._brightness = value
            self.lcd.write(BRIGHTNESS.format(chr(self._brightness)))
    
    def contrast(self, value):
        pass
    
    def rgb(self, r,g,b):
	pass

    def linefeed(self):
        self.lcd.write('\n')

    def write(self, value):
        self.lcd.write(value)

    def close(self):
        self.lcd.close()

if __name__ == '__main__':
    import sys
    import time
    try:
        lcd = adaLCD(sys.argv[1])
    except:
        lcd = adaLCD('/dev/tty.usbmodem411')
    lcd.backlight_on()
    lcd.clear()
    lcd.write('Hello\n\rWorld!')
    lcd.rgb(255,0,0)
    time.sleep(1)
    lcd.rgb(0,255,0)
    time.sleep(1)
    lcd.rgb(0,0,255)
    time.sleep(5)
    lcd.clear()
    lcd.backlight_off()
    lcd.close()

