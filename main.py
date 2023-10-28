#!/usr/bin/python3

from gpiozero import LED
from time import sleep

red = LED(11)
green = LED(13)
blue = LED(15)
sleeptime = .25
while True:
    red.on()
    sleep(sleeptime)
    red.off()
    sleep(sleeptime)

    green.on()
    sleep(sleeptime)
    green.off()
    sleep(sleeptime)

    blue.on()
    sleep(sleeptime)
    blue.off()
    sleep(sleeptime)


# red.blink()

print("Hello World!")

print("Round One, Fight!")
