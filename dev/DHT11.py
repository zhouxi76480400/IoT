try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Cannot import RPi.GPIO")
import time


def delay_us(delay_time):
    delay_us_now_time = time.time()
    while time.time() - delay_us_now_time < delay_time / 1000 / 1000:
        continue


def delay_ms(delay_time):
    delay_ms_now_time = time.time()
    while time.time() - delay_ms_now_time < delay_time / 1000:
        continue


def delay_s(delay_time):
    delay_s_now_time = time.time()
    while time.time() - delay_s_now_time < delay_time:
        continue


channel = 17  # means gpio0


class DHT11(object):
    _instance = None

    def __init__(self):
        print("init HHT11 Weather Sensor")

    # singleton
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DHT11, cls).__new__(cls)
        return cls._instance

    def start_refresh(self):
        self.init_gpio()
        while True:
            self.do_refresh()
        self.clean_gpio()

    def init_gpio(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    def clean_gpio(self):
        GPIO.setup(channel, GPIO.IN)
        GPIO.input(channel, GPIO.LOW)
        # GPIO.cleanup()

    def do_refresh(self):
        GPIO.setup(channel, GPIO.OUT)
        GPIO.output(channel, GPIO.HIGH)
        delay_s(3)
        GPIO.setup(channel, GPIO.OUT)
        GPIO.output(channel, GPIO.LOW)
        delay_ms(25)
        GPIO.output(channel, GPIO.HIGH)
        GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        delay_us(27)

        data_array = []
        humidity = -1
        if GPIO.input(channel) == GPIO.LOW:
            while GPIO.input(channel) != GPIO.HIGH:
                continue
            for i in range(40):
                wait_time_t = time.time()
                while GPIO.input(channel) == GPIO.HIGH:
                    if time.time() - wait_time_t > 1:
                        delay_s(3)
                        return
                    continue
                while GPIO.input(channel) != GPIO.HIGH:
                    if time.time() - wait_time_t > 1:
                        delay_s(3)
                        return
                    continue
                delay_us(32)
                data_array.append(str(GPIO.input(channel)))

            # check is ok?

            str_humidity_high = str().join(data_array[0:8])
            str_humidity_low = str().join(data_array[8:16])
            str_temp_high = str().join(data_array[16:24])
            str_temp_low = str().join(data_array[24:32])
            check_sum = str().join(data_array[32:40])

            humidity_int_high = int(str_humidity_high, 2)
            humidity_int_low = int(str_humidity_low, 2)
            humidity_int_all = humidity_int_high + humidity_int_low
            temp_int_high = int(str_temp_high, 2)
            temp_int_low = int(str_temp_low, 2)
            temp_int_all = temp_int_high + temp_int_low
            check_sum_int_all = int(check_sum, 2)

            if humidity_int_all + temp_int_all == check_sum_int_all:
                print("humidity:" + str(humidity_int_high) + "." + str(humidity_int_low) + "   temp:" + str(
                    temp_int_high) + "." + str(temp_int_low))
            else:
                print("fail")
        else:
            print("fail")
        delay_s(3)
        return

    pass




