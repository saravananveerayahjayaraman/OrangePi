import lcddriver
from time import *
import rdm6300

lcd=lcddriver.lcd()
lcd.lcd_clear()
rdm6300_reader=rdm6300.RDM6300('/dev/serial0')

lcd.lcd_display_string("Tutorial", 1)
lcd.lcd_display_string("Raspberry Pi", 2)
lcd.lcd_display_string("I2C", 3)
lcd.lcd_display_string("HD44780 Driver", 4)

rdm6300_reader.do_work()

lcd.lcd_display_string("Driver", 4)
