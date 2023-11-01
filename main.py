#!/usr/bin/python3
# 3-Color LED with a Raspberry Pi Model 2 B
# written by Matthew Greene


# from gpiozero import LED
from gpiozero import RGBLED
from time import sleep
import random as rdm

# Initialize GPIO Board values
led = RGBLED(red=17, green=27, blue=22)


def led2(x, y, z):
    led.color = (x, y, z)


def led1():  # first iteration of code for historic purposes
    while True:
        red.on()
        sleep(speed)
        red.off()
        sleep(speed)

        green.value = 0.125
        green.on()
        sleep(speed)
        green.off()
        sleep(speed)

        blue.value = 0.5
        blue.on()
        sleep(speed)
        blue.off()
        sleep(speed)


def main():
    print("Hello World!")
    print("Round One, Fight!")
    red = 1
    green = 1
    blue = 1
    speed = .25
    blink = True

    # red.blink()

    while True:
        red = rdm.randrange(0, 100, 1)
        green = rdm.randrange(0, 100, 1)
        blue = rdm.randrange(0, 100, 1)
        led2(red/100,green/100,blue/100)
        sleep(speed)
        led2(0,0,0)
        sleep(speed)
   
   return


if __name__ == '__main__':
    main()