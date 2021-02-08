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



    def __init__(self, speed_pin, ain0_pin, ain1_pin, event):
        self._speed_pin = GPIO(GPIO.get_gpio_pin(speed_pin), 'out')
        self._ain0_pin = GPIO(GPIO.get_gpio_pin(ain0_pin), 'out')
        self._ain1_pin = GPIO(GPIO.get_gpio_pin(ain1_pin), 'out')
        self._ain0_pin.write(0)
        self._ain1_pin.write(0)
        self.speed = 0
        self.set_duty_cycle(self.speed)
        self.in_queue = Queue(1)
        self.out_queue = Queue(1)
        self.direction = Direction.FORWARD
        self.event = event
        self._speed_pin.write(1)

    def set_direction(self, direction_queue):
        new_dir = direction_queue.get()
        if 0 > new_dir > 1:
            print("Direction must be 0 or 1.")
        self.direction = new_dir

        if self.direction == Direction.FORWARD:
            self._ain0_pin.write(1)
            self._ain1_pin.write(0)
        elif self.direction == Direction.BACKWARD:
            self._ain0_pin.write(0)
            self._ain1_pin.write(1)
        elif self.direction == Direction.BRAKE:
            self._ain0_pin.write(1)
            self._ain1_pin.write(1)

    def motor_on(self, speed_queue):
        """
        Starts the pwm signal to the motor as defined during its instantiation. It takes one queue which the
        caller can use to change the speed of the motor. The pwm signal can be stopped by setting the Event
        that was created during instantiation.
        :param speed_queue:
        """

        while 1:
            if not speed_queue.empty():
                self.speed = speed_queue.get()
                self.set_duty_cycle(self.speed)
            self._speed_pin.write(1)
            time.sleep(self._pwm_on_time)
            self._speed_pin.write(0)
            time.sleep(self._pwm_off_time)

            if self.event.is_set():
                break

    def motor_off(self):
        self.event.set()
