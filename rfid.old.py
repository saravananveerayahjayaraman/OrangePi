import codecs
import binascii
import time
import serial
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.output(23,False)
GPIO.output(24,False)
PortRF = serial.Serial('/dev/serial0',9600)
while True:
   ID = ""
   read_byte = PortRF.read()
   if read_byte=="\x02":
      for Counter in range(12):
         read_byte=PortRF.read()
         ID = ID + str(read_byte)
         print hex(ord(read_byte))
         print int(ord(read_byte))
         print ord(read_byte)
         print chr(ord(read_byte))
      maincardno=str(int(ID[2:10],16))
      seccardno=int(ID[2:6],16)
      thdcardno=int(ID[6:10],16)
      main_cardno=maincardno.rjust(10,'0')
      print ID
      print maincardno, seccardno, thdcardno
      print main_cardno
