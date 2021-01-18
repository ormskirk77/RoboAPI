from accelerometer import Accelerometer
from thermometer import Thermometer
from imu import Imu


class Robo:

    imu = Imu()
    thermometer = Thermometer()
    accelerometer = Accelerometer()

    def initialiseImu(self):
        self.imu.initialiseIMU()



