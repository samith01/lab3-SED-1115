from machine import Pin
import time

led1 = Pin(17, Pin.OUT)
sw5 = Pin(22, Pin.IN, Pin.PULL_DOWN)
state = False
led1.value(0)

while True:
    if sw5.value() and state == False :
        time.sleep(0.5)
        while sw5.value(): # wait till we release the button
            pass
        ## button released
        led1.value(1)
        state = True
       
    if sw5.value() and state == True :
        time.sleep(0.5)
        while sw5.value(): # wait till we release the button
            pass
        ## button released
        led1.value(0)
        state = False

