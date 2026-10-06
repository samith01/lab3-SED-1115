from machine import Pin

led1 = Pin(6, Pin.OUT)
led2 = Pin(7, Pin.OUT)
led3 = Pin(8, Pin.OUT)
led4 = Pin(9, Pin.OUT)

sw1 = Pin(10, Pin.IN, Pin.PULL_DOWN)
sw2 = Pin(11, Pin.IN, Pin.PULL_DOWN)
sw3 = Pin(12, Pin.IN, Pin.PULL_DOWN)
sw4 = Pin(13, Pin.IN, Pin.PULL_DOWN)

leds = [led1,led2,led3,led4]
sws = [sw1,sw2,sw3,sw4]

while True:
    for i in range(len(sws)):
        if sws[i].value():
            leds[i].value(1)
        else:
            leds[i].value(0)
        