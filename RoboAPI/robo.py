from thermometer import Thermometer
from imu import Imu


class Robo:

    imu = Imu()
    thermometer = Thermometer()

    def initialiseImu(self):
        self.imu.initialiseIMU()



