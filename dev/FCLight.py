try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Cannot import RPi.GPIO")
import time

fc_light_gpio_channel = 18  # gpio1

fc_light_fresh_rate = 0.5  # sec


class FCLight(object):

    # high status
    FCLightHigh = False

    # low status
    FCLightLow = True

    fc_light_now_status = FCLightLow

    is_stop = False

    # return now status
    def get_light_status(self):
        return self.fc_light_now_status

    _instance = None

    def __init__(self):
        print("init FC Light")

    # singleton
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(FCLight, cls).__new__(cls)
        return cls._instance

    def init_gpio(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(fc_light_gpio_channel, GPIO.IN)

    def clean_gpio(self):
        GPIO.cleanup(fc_light_gpio_channel)

    def start_service(self):
        if not self.is_stop:
            self.init_gpio()
            while not self.is_stop:
                time.sleep(fc_light_fresh_rate)
                self.update_light_status()

            self.clean_gpio()

    def update_light_status(self):
        status_tmp = GPIO.input(fc_light_gpio_channel)
        if status_tmp != self.fc_light_now_status:
            self.fc_light_now_status = status_tmp
            status_name = "High"
            if self.fc_light_now_status == FCLight.FCLightLow:
                status_name = "Low"
            print("FC Light new status :" + status_name)

    def stop_service(self):
        self.is_stop = False

    pass
