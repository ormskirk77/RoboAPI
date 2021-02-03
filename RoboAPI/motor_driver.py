from driver import Driver
import time, threading
from direction import Direction
from pynq import GPIO
import time
from threading import Event
from queue import Queue

class MotorDriver(Driver):
    # PS frequency possibly 500MHz or 1200MHz.
    # Forward:  AIN0 -> HIGH, AIN1 -> LOW
    # Backward: AIN0 -> LOW,  AIN1 -> HIGH
    # Brake:    AIN0 -> HIGH,  AIN1 -> HIGH


    speed = 0
    direction = Direction.FORWARD

    def __init__(self, pin):
        self._pin = GPIO(GPIO.get_gpio_pin(pin), 'out')
        self.event = Event()
        self.speed = 0
        self.in_queue = Queue(1)
        self.out_queue = Queue(1)

    def motor_on(self):
        """
        call motor_on() and this will instigate a new thread and listen for changes in the direction, and speed
        of the motor.
        """
        motor_thread = threading.Thread(target=self.pwm_start)
        motor_thread.start()
        print(threading.activeCount())



    def pwm_start(self):
        # self.set_duty_cycle(duty_cycle)
        # print("Motor on")
        while 1:
            self._pin.write(1)
            time.sleep(self._pwm_on_time)
            self._pin.write(0)
            time.sleep(self._pwm_off_time)
