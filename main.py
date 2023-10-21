#!/usr/bin/python3

from gpiozero import LED
from time import sleep

led = LED(24)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)

red.blink()

print("Hello World!")

print("Round One, Fight!")
