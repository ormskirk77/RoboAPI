from driver import Driver
import mraa, time
from pynq import Overlay

class MotorDriver(Driver):

    def __init__(self):
     #   pin = mraa.mraa_gpio_init_raw(338)
        pin = mraa.Gpio(338, raw=True)
        x = pin.getPin()

        # x = mraa.Pwm(338)
        #
        # # set PWM period
        # x.period_us(700)
        #
        # # enable PWM
        # x.enable(True)
        #
        # value = 0.0
        #
        # while True:
        #     # write PWM value
        #     x.write(value)
        #
        #     time.sleep(0.05)
        #
        #     value = value + 0.01
        #     if value >= 1:
        #         value = 0.0
        #
