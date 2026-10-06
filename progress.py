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
    
    if value >=0:
        led2.value(1)
        led3.value(0)
        led4.value(0)
        led5.value(0)
        
    if value >=16383:
        led2.value(1)
        led3.value(1)
        led4.value(0)
        led5.value(0)
    
    if value >= 32766:
        led2.value(1)
        led3.value(1)
        led4.value(1)
        led5.value(0)
        
    if value >= 49149:
        led2.value(1)
        led3.value(1)
        led4.value(1)
        led5.value(1)
    
        
   
	time.sleep_ms(50)