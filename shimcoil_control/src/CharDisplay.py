'''
Created on May 16, 2018

@author: klein
this is the class controlling the chracater display
the connection depensd on which GPIO are connetec from the raspi
'''

from Adafruit_CharLCD import Adafruit_CharLCD
from cgitb import enable
import time


class MyDisplay(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
        # the next assignment connenct the raspi to the adafruit
        RSE = 21
        ENABLEIO = 20
        GPIO1 = 16
        GPIO2 = 12
        GPIO3 = 7
        GPIO4 = 8
        self.lcd = Adafruit_CharLCD(rs=RSE,
                                     en=ENABLEIO,
                                      d4=GPIO1, d5=GPIO2, d6=GPIO3, d7=GPIO4,cols=16, lines=2)
    
if __name__ == '__main__':
    lcd = MyDisplay()
    lcd.clear()
    lcd.message('start') 
    time.sleep(5)
    lcd.set_cursor(1,2)
    lcd.blink(True)
    lcd.message('goodbye')