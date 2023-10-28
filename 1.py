#!/usr/bin/python3

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

LEDpin = 26
buttonPin = 21

GPIO.setup(LEDpin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(LEDpin, False)

try:
    while True:
        GPIO.output(LEDpin, not GPIO.input(buttonPin))
        sleep(0.1)

finally:
    GPIO.output(LEDpin, False)
    GPIO.cleanup()