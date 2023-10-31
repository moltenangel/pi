#!/usr/bin/python3
# 3-Color LED with a Raspberry Pi Model 2 B
# written by Matthew Greene


# from gpiozero import LED
from gpiozero import PWMLED
from time import sleep

# red = LED(11)
# green = LED(13)
# blue = LED(15)
red = PWMLED(11)
green = PWMLED(13)
blue = PWMLED(15)
sleeptime = .25

while True:
    red.on()
    sleep(sleeptime)
    red.off()
    sleep(sleeptime)

    green.value = 0.125
    green.on()
    sleep(sleeptime)
    green.off()
    sleep(sleeptime)

    blue.value = 0.5
    blue.on()
    sleep(sleeptime)
    blue.off()
    sleep(sleeptime)


# red.blink()

print("Hello World!")

print("Round One, Fight!")
