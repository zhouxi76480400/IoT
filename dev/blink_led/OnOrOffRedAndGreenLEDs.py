import RPi.GPIO as GPIO
import sys

gpio_red_led_port_number = 26
gpio_green_led_port_number = 12
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def close_all_leds():
    GPIO.setup(gpio_red_led_port_number, GPIO.OUT)
    GPIO.setup(gpio_green_led_port_number, GPIO.OUT)
    GPIO.output(gpio_red_led_port_number, GPIO.LOW)
    GPIO.output(gpio_green_led_port_number, GPIO.LOW)


def on_or_off_led(port, is_on):
    GPIO.setup(port, GPIO.OUT)
    if is_on:
        GPIO.output(port, GPIO.HIGH)
    else:
        GPIO.output(port, GPIO.LOW)


def on_or_off_green_led(is_on):
    on_or_off_led(gpio_green_led_port_number, is_on)


def on_or_off_red_led(is_on):
    on_or_off_led(gpio_red_led_port_number, is_on)


argv = sys.argv
args = len(sys.argv)

if args < 3:
    close_all_leds()
    exit(0)
else:
    close_all_leds()
    is_red_led_on = bool(int(argv[1]))
    is_green_led_on = bool(int(argv[2]))
    print('is_red_led_on:'+str(is_red_led_on)+'\tis_green_led_on:'+str(is_green_led_on))
    if is_red_led_on is False and is_green_led_on is False:
        close_all_leds()
    else:
        on_or_off_green_led(is_green_led_on)
        on_or_off_red_led(is_red_led_on)
