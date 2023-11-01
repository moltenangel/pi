#!/usr/bin/python3
# 3-Color LED with a Raspberry Pi Model 2 B
# written by Matthew Greene


# from gpiozero import LED
from gpiozero import RGBLED
from time import sleep

red = LED(17)
green = LED(27)
blue = LED(22)
led = RGBLED(red=17, green=27, blue=22)
sleeptime = .25


def ledtest(x, y, z):
    led.color = (x, y, z)


def ledblink():
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


if __name__ == '__main__':
    while True:
        ledtest(0,0,0)
        sleep(sleeptime)
        ledtest(1,1,1)
        sleep(sleeptime)