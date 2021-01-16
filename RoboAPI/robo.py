from motor_driver import MotorDriver
from thermometer import Thermometer
from servoDriver import ServoDriver
from accelerometer import Accelerometer
import imu


class Robo:


    thermometer = Thermometer()
 #   motor1 = MotorDriver()
 #   servoDriver = ServoDriver()
 #   accelerometer = Accelerometer()

    def initialiseImu(self):
        self.thermometer.initialise()



