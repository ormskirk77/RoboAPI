import time
from queue import Queue
from RoboAPI.driver import Driver
from pynq import GPIO


class ServoDriver(Driver):
    '''
    Servo specific code.
    '''
    def __init__(self, control_pin, max_position, event):
        self.event = event
        self._control_pin = GPIO(GPIO.get_gpio_pin(control_pin), 'out')
        self.position = 0
        self.max_position = max_position
        self.in_queue = Queue(1)
        self.out_queue = Queue(1)

    def set_new_position(self, new_position_queue):
        while 1:
            if not new_position_queue.empty():
                # Calculate the new position as a proportion of the max position for the servo, then set the duty cycle based on this.
                self.position = new_position_queue.get()
                new_duty_cycle = (self.position/self.max_position)*100
                self.set_duty_cycle(new_duty_cycle)
            self._control_pin.write(1)
            time.sleep(self._pwm_on_time)
            self._control_pin.write(0)
            time.sleep(self._pwm_off_time)
            time.sleep(self._pwm_off_time)

            if self.event.is_set():
                break

