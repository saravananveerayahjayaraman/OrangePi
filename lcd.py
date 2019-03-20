from Adafruit_CharLCD import Adafruit_CharLCD # Importing Adafruit library for LCD
from time import sleep  # Importing sleep from time library to add delay in program

# instantiate lcd and specify pins
lcd = Adafruit_CharLCD(rs=7, en=8, d4=25, d5=24, d6=23, d7=18, cols=16, lines=2)
lcd.clear()
# display text on LCD, \n = new line
lcd.message('Welcome to\nElectronicshobbyists.com')
sleep(3)

lcd.clear()
lcd.message('  Type Anything\n')
text = raw_input('Type Anything\n')  #Getting input from user
# For python 3, Use the below command to get the user input
# text = input('  Type Anything\n')
lcd.message(text)
sleep(5)

# Clear the screen
lcd.clear()
