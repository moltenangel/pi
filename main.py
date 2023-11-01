#!/usr/bin/python3
# 3-Color LED with a Raspberry Pi Model 2 B
# written by Matthew Greene


# from gpiozero import LED
from gpiozero import RGBLED
from time import sleep
import random as rdm

# Initialize GPIO Board values
led = RGBLED(red=17, green=27, blue=22)


def led1(x, y, z):
    led.color = (x, y, z)


def main():
    print("Hello World!")
    print("Round One, Fight!")
    red = 1
    green = 1
    blue = 1
    speed = .03
    mode = 1
    maxspeed = 50


    def blink():
        red = rdm.randrange(0, 100, 1) / 100
        green = rdm.randrange(0, 100, 1) / 100
        blue = rdm.randrange(0, 100, 1) / 100
        speed = rdm.randrange(0, maxspeed, 1) / 100
        blinkrate = rdm.randrange(0, 100, 1) / 100
        led1(red, green, blue)
        sleep(speed)
        if blinkrate >= .50:
            led1(0,0,0)
            sleep(speed)

    while True:
        blink()


if __name__ == '__main__':
    main()