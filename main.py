from ICM20948 import ICM20948
from RoboAPI.robo import Robo
import os

print(os.getcwd())
robo = Robo()

robo.initialiseImu()

# print("Temp: " + str(robo.thermometer.getTemperature()))
# print("Accel: " + str(robo.accelerometer.getScaledData()))

# imu = ICM20948()
#
# temp = imu.read_temperature()
# print("Temp: " + str(temp) + "\n")
#
# x, y, z = imu.read_magnetometer_data()
# ax, ay, az, gx, gy, gz = imu.read_accelerometer_gyro_data()
#
# print("""
# Accel: {:05.2f} {:05.2f} {:05.2f}
# Gyro:  {:05.2f} {:05.2f} {:05.2f}
# Mag:   {:05.2f} {:05.2f} {:05.2f}""".format(
#     ax, ay, az, gx, gy, gz, x, y, z
# ))