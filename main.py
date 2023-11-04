#!/usr/bin/python3
# 3-Color LED controlled by a rotary encoder with a Raspberry Pi Model 2 B
# written by Matthew Greene
# 11/3/23
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
rotor = RotaryEncoder(24, 18, wrap=True)  #  maxsteps=totalsteps/2
rotor.steps = -(totalsteps/2)  # -180
led = RGBLED(red=17, green=27, blue=22, active_high=False)
btn = Button(23)  # pull_up=False)
done = Event()


def main():
    print("Raspberry Pi device")
    print("Round One, Fight!")
    speed = .03
    maxspeed = 50
    mode = 0
    hue = (rotor.steps + totalsteps / 2) / totalsteps

    def change_mode():
        global totalsteps
        nonlocal mode
        nonlocal hue

        mode += 1
        print(f'mode={mode}')

        if mode == 1:
            print('blink')
            led.blink(on_time=1, off_time=1, fade_in_time=0, fade_out_time=0, on_color=Color(h=hue, s=1, v=1), off_color = (0, 0, 0), n=None, background=True)
        elif mode == 2:
            print('pulse')
            led.pulse(fade_in_time=1, fade_out_time=0, on_color=Color(h=hue, s=1, v=1), off_color=(0, 0, 0), n=None, background=True)
        else:
            print('mode=0')
            mode = 0
            led.on()
            led.color = Color(h=hue, s=1, v=1)

    def rdm_color():
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
        print(f'rotor.steps={rotor.steps}' | print(f,'totalsteps={totalsteps}'))
        nonlocal hue
        hue = (rotor.steps + totalsteps/2) / totalsteps
        if led.is_lit == True:
            led.color = Color(h=hue, s=1, v=1)

    def show_color():
        print(f'Hue {led.color.hue.deg:.1f} degrees = {led.color.html}')
#            change_mode()

    def stop_script():
        print('Exiting')
        done.set()

    print('Select a color by turning the knob')
    print('Select a color by turning the knob')
    print('Hold the button to exit')
    print('Goodbye...')

    # Event Handler
    rotor.when_rotated = change_hue
    btn.when_pressed = show_color  # led_toggle
    btn.when_released = change_mode  # show_color
    btn.when_held = led.toggle  # stop_script
    done.wait()
    print('Goodbye...')


if __name__ == '__main__':
    main()
