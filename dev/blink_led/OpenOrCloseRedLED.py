# import RPi.GPIO as GPIO
# import time
# import signal
#
#
# def sigint_handler(signum, frame):
#   global is_sigint_up
#   is_sigint_up = True
#   print ('catched interrupt signal!')
#   GPIO.cleanup()
#   exit(0)
#
#
# signal.signal(signal.SIGINT, sigint_handler)
# signal.signal(signal.SIGHUP, sigint_handler)
# signal.signal(signal.SIGTERM, sigint_handler)
# is_sigint_up = False
#
#
# gpio_red_led_port_number = 26
# gpio_green_led_port_number = 12
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# GPIO.setup(gpio_red_led_port_number, GPIO.OUT)
# GPIO.setup(gpio_green_led_port_number, GPIO.OUT)
# GPIO.output(gpio_red_led_port_number, GPIO.HIGH)
# GPIO.output(gpio_green_led_port_number, GPIO.LOW)
#
# global is_light_open
# is_light_open = True
#
# def do_something(is_light_open):
#     if is_light_open:
#         GPIO.output(gpio_red_led_port_number, GPIO.LOW)
#         GPIO.output(gpio_green_led_port_number, GPIO.HIGH)
#     else:
#         GPIO.output(gpio_red_led_port_number, GPIO.HIGH)
#         GPIO.output(gpio_green_led_port_number, GPIO.LOW)
#
# while True:
#     do_something(is_light_open)
#     time.sleep(1)
#     if is_light_open:
#         is_light_open = False
#     else:
#         is_light_open = True
#
#
#


import sys
import os

os.system('python3 ./dev/blink_led/OnOrOffRedAndGreenLEDs.py 1 0')


