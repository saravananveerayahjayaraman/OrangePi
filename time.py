#!/usr/bin/python
from time import *
import lcddriver
import time

lcd=lcddriver.lcd()

lcd.lcd_clear()

try:
   while True:
      lcd.lcd_display_string('PYRO TECHNOLOGY',1)
      lcd.lcd_display_string(time.strftime('%H:%M:%S'),3)

except KeyboardInterrupt:
   pass
   exit()
