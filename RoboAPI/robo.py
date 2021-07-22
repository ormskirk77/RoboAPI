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
    '''
    The Robo class contains all of the functionailty of the Robo96 board. It starts off with two motors and 8 servos ready to be
    controlled. If you want fewer of these you will need to uncomment them in the __init__ method below. This is a good idea, as
    each motor/servo runs in its own thread.
    '''
    def __init__(self):
        self.imu = Imu()
        # thermometer = Thermometer()
        # accelerometer = Accelerometer()
        # TODO: Write function to return a motor driver, its speed queue, direction queue and its thread.

        # Motor 1 setup:
        self.motor1_e = Event()
        self.motor1_speed_pin = 8
        self.motor1_ain0_pin = 12
        self.motor1_ain1_pin = 13
        self.motor1 = MotorDriver(self.motor1_speed_pin, self.motor1_ain0_pin, self.motor1_ain1_pin, self.motor1_e)
        self.motor1_speed_queue = Queue(1)
        self.motor1_speed_queue.put(0)
        self.motor1_direction_queue = Queue(1)

        self.motor1_thread = Thread(name="motor1", target=self.motor1.motor_on, args=(self.motor1_speed_queue,), daemon=True)
        self.motor1_thread.start()

        # Motor 2 setup:
        self.motor2_e = Event()
        self.motor2_speed_pin = 9
        self.motor2_ain0_pin = 11
        # The ain1 pin for motor 2 has an unusual assignment. The FS GPIO pins have base 338.
        #  ain1 for motor 2 corresponds to MIO45. So 338 + 45 = 383.
        #  However, gpio0 = 416. So 416 - 33 = 383.
        self.motor2_ain1_pin = -33
        self.motor2 = MotorDriver(self.motor2_speed_pin, self.motor2_ain0_pin, self.motor2_ain1_pin, self.motor2_e)
        self.motor2_speed_queue = Queue(1)
        self.motor2_speed_queue.put(0)
        self.motor2_direction_queue = Queue(1)

        self.motor2_thread = Thread(name="motor2", target=self.motor2.motor_on, args=(self.motor2_speed_queue,), daemon=True)
        self.motor2_thread.start()

        # # Servo 1
        # self.servo1_control_pin = 0 # Low speed header pin 3 => HD_GPIO_0
        # self.servo1_event = Event()
        # self.servo1_max_position = 180
        # self.servo1_position_queue = Queue(1)
        # self.servo1 = ServoDriver(self.servo1_control_pin, self.servo1_max_position, self.servo1_event)
        #
        # self.servo1_thread = Thread(name="servo1", target=self.servo1.set_new_position, args=(self.servo1_position_queue,), daemon=True)
        # self.servo1_thread.start()
        # #
        # # # Servo 2
        # self.servo2_control_pin = 1 # Low speed header pin 9 => HD_GPIO_3
        # self.servo2_event = Event()
        # self.servo2_max_position = 180
        # self.servo2_position_queue = Queue(1)
        # self.servo2 = ServoDriver(self.servo2_control_pin, self.servo2_max_position, self.servo2_event)
        #
        # self.servo2_thread = Thread(name="servo2", target=self.servo1.set_new_position, args=(self.servo1_position_queue,), daemon=True)
        # self.servo2_thread.start()

        # Servo 3
        self.servo3_control_pin = 2 # Low speed header pin 11 => HD_GPIO_4
        self.servo3_event = Event()
        self.servo3_max_position = 180
        self.servo3_position_queue = Queue(1)
        self.servo3 = ServoDriver(self.servo3_control_pin, self.servo3_max_position, self.servo3_event)

        self.servo3_thread = Thread(name="servo3", target=self.servo3.set_new_position, args=(self.servo3_position_queue,), daemon=True)
        self.servo3_thread.start()

        # Servo 4
        # self.servo4_control_pin = 2 # Low speed header pin 13 => HD_GPIO_5
        # self.servo4_event = Event()
        # self.servo4_max_position = 180
        # self.servo4_position_queue = Queue(1)
        # self.servo4 = ServoDriver(self.servo4_control_pin, self.servo4_max_position, self.servo4_event)
        #
        # self.servo4_thread = Thread(name="servo4", target=self.servo4.set_new_position, args=(self.servo4_position_queue,), daemon=True)
        # self.servo4_thread.start()
        #
        # # Servo 5
        # self.servo5_control_pin = 4 # Low speed header pin 29 => HD_GPIO_6
        # self.servo5_event = Event()
        # self.servo5_max_position = 180
        # self.servo5_position_queue = Queue(1)
        # self.servo5 = ServoDriver(self.servo5_control_pin, self.servo5_max_position, self.servo5_event)
        #
        # self.servo5_thread = Thread(name="servo5", target=self.servo5.set_new_position, args=(self.servo5_position_queue,), daemon=True)
        # self.servo5_thread.start()

        # Servo 6
        # self.servo6_control_pin = 5 # Low speed header pin 31 => HD_GPIO_7
        # self.servo6_event = Event()
        # self.servo6_max_position = 180
        # self.servo6_position_queue = Queue(1)
        # self.servo6 = ServoDriver(self.servo6_control_pin, self.servo6_max_position, self.servo6_event)
        #
        # self.servo6_thread = Thread(name="servo6", target=self.servo6.set_new_position, args=(self.servo6_position_queue,), daemon=True)
        # self.servo6_thread.start()
        #
        # # Servo 7
        # self.servo7_control_pin = 6 # Low speed header pin 33 => HD_GPIO_8
        # self.servo7_event = Event()
        # self.servo7_max_position = 180
        # self.servo7_position_queue = Queue(1)
        # self.servo7 = ServoDriver(self.servo7_control_pin, self.servo7_max_position, self.servo7_event)
        #
        # self.servo7_thread = Thread(name="servo7", target=self.servo7.set_new_position, args=(self.servo7_position_queue,), daemon=True)
        # self.servo7_thread.start()
        #
        # # Servo 8
        # self.servo8_control_pin = 7 # Low speed header pin 16 => HD_GPIO_9
        # self.servo8_event = Event()
        # self.servo8_max_position = 180
        # self.servo8_position_queue = Queue(1)
        # self.servo8 = ServoDriver(self.servo8_control_pin, self.servo8_max_position, self.servo8_event)
        #
        # self.servo8_thread = Thread(name="servo8", target=self.servo8.set_new_position, args=(self.servo8_position_queue,), daemon=True)
        # self.servo8_thread.start()

    def set_servo_position(self, servo_id, new_position):
        """
        Use this function to change the position of a servo motor. Its arguments are the servo_id and the position for the servo to move to.
        :param servo_id: An int from 1-8 to specify which servo to move
        :param new_position: The new position to move to.
        :return:
        """
        if servo_id == 1:
            self.servo1_position_queue.put(new_position)
        elif servo_id == 2:
            self.servo2_position_queue.put(new_position)
        elif servo_id == 3:
            self.servo3_position_queue.put(new_position)
        elif servo_id == 4:
            self.servo4_position_queue.put(new_position)
        elif servo_id == 5:
            self.servo5_position_queue.put(new_position)
        elif servo_id == 6:
            self.servo6_position_queue.put(new_position)
        elif servo_id == 7:
            self.servo7_position_queue.put(new_position)
        elif servo_id == 8:
            self.servo8_position_queue.put(new_position)

    def set_motor_speed(self, motor_id, new_speed):
        """
        Changes the specified motors speed.
        :param motor_id: int 1, 2 or 3. Specifies an individual motor, or both motors (motor_id = 3)
        :param new_speed: int, 1 - 100.
        :return:
        """
        if motor_id == 1:
            self.motor1_speed_queue.put(new_speed)
        elif motor_id == 2:
            self.motor2_speed_queue.put(new_speed)
        elif motor_id == 3:
            self.motor1_speed_queue.put(new_speed)
            self.motor2_speed_queue.put(new_speed)

    def set_motor_direction(self, motor_id, new_direction):
        """
        Changes the direction of the specified motor. Its arguments are the motor_id and its new direction
        :param motor_id: int 1, 2 or 3. Specifies an individual motor, or both motors (motor_id = 3)
        :param new_direction:
        :return:
        """
        if motor_id == 1:
            self.motor1_direction_queue.put(new_direction)
            self.motor1.set_direction(self.motor1_direction_queue)
        elif motor_id == 2:
            self.motor2_direction_queue.put(new_direction)
            self.motor2.set_direction(self.motor2_direction_queue)
        elif motor_id == 3:
            self.motor1_direction_queue.put(new_direction)
            self.motor1.set_direction(self.motor1_direction_queue)
            self.motor2_direction_queue.put(new_direction)
            self.motor2.set_direction(self.motor2_direction_queue)

    def initialiseImu(self):
        self.imu.initialiseIMU()



