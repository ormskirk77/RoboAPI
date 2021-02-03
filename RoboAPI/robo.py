from accelerometer import Accelerometer
from motor_driver import MotorDriver
from thermometer import Thermometer
from imu import Imu
from pynq import Overlay
from queue import Queue


vcs_overlay = Overlay("./vcs-jnr-pynq/vcs_jnr_pynq.bit")


class Robo:

    imu = Imu()
    # thermometer = Thermometer()
    # accelerometer = Accelerometer()

    motor1 = MotorDriver(8)
    motor1.motor_on()


    def initialiseImu(self):
        self.imu.initialiseIMU()



