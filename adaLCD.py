#!/usr/bin/python
import serial

BACKLIGHT_ON = chr(0xFE) + chr(0x42) + chr(255 )
BACKLIGHT_OFF = chr(0xFE) + chr(0x46)
BRIGHTNESS = chr(0xFE) + chr(0x99) + '{0}'
CONTRAST = chr(0xFE) + chr(0x50) + '{0}'
CLEAR = chr(0xFE) + chr(0x58)
RGB = chr(0xFE) + chr(0xD0) + '{0}{1}{2}'
HOME = chr(0xFE) + chr(0x48)

class adaLCD(object):
    def __init__(self, port):
        self.lcd = serial.Serial(port, 9600)

        self._brightness = 0
        self._contrast = 0
        self._rgb = []
    
    def clear(self):
        self.lcd.write(CLEAR)
    
    def home(self):
        self.lcd.write(HOME)

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
        if self._contrast == value:
            return
        else:
            self._contrast = value
            self.lcd.write(CONTRAST.format(chr(self._contrast)))
    
    def rgb(self, r,g,b):
        if self._rgb == [r,g,b]:
            return
        else:
            self._rgb = [r,g,b]
            self.lcd.write(RGB.format(chr(r), chr(g), chr(b)))

    def write(self, value):
        self.lcd.write(value)
    
    def linefeed(self):
        self.lcd.write('\n\r')

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

