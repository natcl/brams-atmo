#!/usr/bin/python

import os
import time
from sparkfunLCD import sparkfunLCD

lcd = sparkfunLCD('/dev/ttyAMA0')
lcd.clear()

ip = os.popen('ip addr show eth0 | grep inet').read().split()[1].split('/')[0]
lcd.clear()
lcd.write(ip)
time.sleep(10)
lcd.close()
