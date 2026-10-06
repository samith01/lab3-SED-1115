from machine import Pin, PWM, ADC
import time

adcA = ADC(Pin(26))
led1 = PWM(Pin(17))
led1.freq(1000)

led2 = Pin(6, Pin.OUT)
led3 = Pin(7, Pin.OUT)
led4 = Pin(8, Pin.OUT)
led5 = Pin(9, Pin.OUT)



x = 0
increasing = True
while True:
    value = adcA.read_u16()
   
    led1.duty_u16(x)
    if increasing:
        x += 1
    else:
        x -= 1
    if x == 65535:
        increasing = False
    if x == 0:
        increasing = True
    
	time.sleep_ms(50)