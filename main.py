#!/usr/bin/python3
# 3-Color LED controlled by a rotary encoder with a Raspberry Pi Model 2 B
# written by Matthew Greene
# 11/2/23
# References:
# Rotary Encoder: https://github.com/gpiozero/gpiozero/blob/master/gpiozero/input_devices.py#L982

# from gpiozero import LED
from gpiozero import RGBLED, RotaryEncoder, Button
from colorzero import Color
from threading import Event
from time import sleep
import random as rdm

# Initialize GPIO Board values
totalsteps = 90  # default = 360
# led = RGBLED(red=17, green=27, blue=22, active_high=False)
#rotor = RotaryEncoder(24, 18, wrap=True, maxsteps=totalsteps/2)
rotor = RotaryEncoder(24, 18, wrap=True,)  #  maxsteps=totalsteps/2
rotor.steps = -(totalsteps/2)  # -180
btn = Button(23)  # btn = Button(23, pull_up=False)
done = Event()

def main():
    print("Hello World!")
    print("Round One, Fight!")
    speed = .03
    maxspeed = 50

    def blink():
        red = rdm.randrange(0, totalsteps, 1) / totalsteps
        green = rdm.randrange(0, totalsteps, 1) / totalsteps
        blue = rdm.randrange(0, totalsteps, 1) / totalsteps
        speed = rdm.randrange(0, maxspeed, 1) / totalsteps
        blinkrate = rdm.randrange(0, totalsteps, 1) / totalsteps
        led.color = (red, green, blue)
        sleep(speed)
        if blinkrate >= .25:
            led.color = (0,0,0)
            sleep(speed)

        def change_hue():
            # Scale the rotor steps (-180..180) to 0..1
            hue = (rotor.steps + totalsteps/2) / totalsteps
            led.color = Color(h=hue, s=1, v=1)

        def show_color():
            print(f'Hue {led.color.hue.deg:.1f} degrees = {led.color.html}')
            blink()

        def stop_script():
            print('Exiting')
            done.set()

        print('Select a color by turning the knob')
        rotor.when_rotated = change_hue
        print('Select a color by turning the knob')
        btn.when_released = show_color
        print('Hold the button to exit')
        btn.when_held = stop_script
        done.wait()
        print('Goodbye...')


if __name__ == '__main__':
