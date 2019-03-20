#!/usr/bin/python
from time import *
import lcddriver
import codecs
import binascii
import time
import serial
import RPi.GPIO as GPIO

lcd=lcddriver.lcd()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.output(12,False)
GPIO.output(16,False)


try:
   while True:
      PortRF = serial.Serial('/dev/serial0',9600)
      ID = ""
      read_byte = PortRF.read()
      if read_byte=="\x02":
         for Counter in range(12):
            read_byte=PortRF.read()
            ID = ID + str(read_byte)
      maincardno=str(int(ID[2:10],16))
      seccardno=str(int(ID[2:6],16))
      thdcardno=str(int(ID[6:10],16))
      main_cardno=maincardno.rjust(10,'0')
      sec_cardno=seccardno.rjust(3,'0')
      thd_cardno=thdcardno.rjust(5,'0')
      #print ID
      #print maincardno, seccardno, thdcardno
      #print main_cardno, sec_cardno, thd_cardno
      print "ID No :" + main_cardno
#      lcd.lcd_display_string(time.strftime('%H:%M:%S'),3)
      lcd.lcd_display_string("ID No : " + main_cardno,4)
      GPIO.output(12,True)
      GPIO.output(16,True)
      time.sleep(.1)
      GPIO.output(12,False)
      GPIO.output(16,False)
      ID=""

except KeyboardInterrupt:
   GPIO.cleanup()
   pass
   exit()
