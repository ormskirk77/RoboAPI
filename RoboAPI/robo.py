from accelerometer import Accelerometer
from motor_driver import MotorDriver
from servo_driver import ServoDriver
from thermometer import Thermometer
from imu import Imu
from pynq import Overlay
from threading import Thread, Event
from queue import Queue


vcs_overlay = Overlay("./vcs-jnr-pynq/vcs_jnr_pynq.bit")


class Robo:
    def __init__(self):
        self.imu = Imu()
        # thermometer = Thermometer()
        # accelerometer = Accelerometer()
        # TODO: Write function to return a motor driver, its speed queue, direction queue and its thread.

        # Motor 1 pins:
        self.motor1_e = Event()
        self.motor1_speed_pin = 8
        self.motor1_ain0_pin = 12
        self.motor1_ain1_pin = 13
        self.motor1 = MotorDriver(self.motor1_speed_pin, self.motor1_ain0_pin, self.motor1_ain1_pin, self.motor1_e)
        self.motor1_speed_queue = Queue(1)
        self.motor1_direction_queue = Queue(1)

        self.motor1_thread = Thread(name="motor1", target=self.motor1.motor_on, args=(self.motor1_speed_queue,), daemon=True)
        self.motor1_thread.start()

        # Motor 2 pins:
        self.motor2_e = Event()
        self.motor2_speed_pin = 8 # Place holder
        self.motor2_ain0_pin = 12 # Place holder
        self.motor2_ain1_pin = 13 # Place holder
        self.motor2 = MotorDriver(self.motor2_speed_pin, self.motor2_ain0_pin, self.motor2_ain1_pin, self.motor2_e)
        self.motor2_speed_queue = Queue(1)
        self.motor2_direction_queue = Queue(1)

        self.motor2_thread = Thread(name="motor2", target=self.motor2.motor_on, args=(self.motor2_speed_queue,), daemon=True)
        self.motor2_thread.start()

        # Servo 1
        self.servo1_control_pin = 0 # Low speed header pin 3 => HD_GPIO_0
        self.servo1_event = Event()
        self.servo1_max_position = 180
        self.servo1_position_queue = Queue(1)
        self.servo1 = ServoDriver(self.servo1_control_pin, self.servo1_max_position, self.servo1_event)

        self.servo1_thread = Thread(name="servo1", target=self.servo1.set_new_position, args=(self.servo1_position_queue,), daemon=True)
        self.servo1_thread.start()

        # Servo 2
        self.servo2_control_pin = 1 # Low speed header pin 9 => HD_GPIO_3
        self.servo2_event = Event()
        self.servo2_max_position = 180
        self.servo2_position_queue = Queue(1)
        self.servo2 = ServoDriver(self.servo2_control_pin, self.servo2_max_position, self.servo2_event)

        self.servo2_thread = Thread(name="servo2", target=self.servo1.set_new_position, args=(self.servo1_position_queue,), daemon=True)
        self.servo2_thread.start()

        # Servo 3
        self.servo3_control_pin = 2 # Low speed header pin 11 => HD_GPIO_4
        self.servo3_event = Event()
        self.servo3_max_position = 180
        self.servo3_position_queue = Queue(1)
        self.servo3 = ServoDriver(self.servo3_control_pin, self.servo3_max_position, self.servo3_event)

        self.servo3_thread = Thread(name="servo3", target=self.servo3.set_new_position, args=(self.servo3_position_queue,), daemon=True)
        self.servo3_thread.start()

    def set_servo1_position(self, new_position):
        self.servo1_position_queue.put(new_position)

    def set_motor1_speed(self, new_speed):
        self.motor1_speed_queue.put(new_speed)

    def set_motor1_direction(self, new_direction):
        self.motor1_direction_queue.put(new_direction)
        self.motor1.set_direction(self.motor1_direction_queue)

    def initialiseImu(self):
        self.imu.initialiseIMU()



