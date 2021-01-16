from ICM20948 import ICM20948
from RoboAPI.robo import Robo


robo = Robo()
#
print("Temp: " + str(robo.thermometer.getTemperature()))
#
#print("Raw accel. : " + str(robo.accelerometer.getRawData()))
#print("Scaled accel. : " + str(robo.accelerometer.getScaledData()))
# # print("Running on host: " + str(socket.gethostname()))
#

#
imu = ICM20948()
# x, y, z = imu.read_magnetometer_data()
# ax, ay, az, gx, gy, gz = imu.read_accelerometer_gyro_data()
temp = imu.read_temperature()
# print("\n\n ICM2098 Library: \n")
print("Temp: " + str(temp) + "\n")
# print("""
# Accel: {:05.2f} {:05.2f} {:05.2f}
# Gyro:  {:05.2f} {:05.2f} {:05.2f}
# Mag:   {:05.2f} {:05.2f} {:05.2f}""".format(
#         ax, ay, az, gx, gy, gz, x, y, z
# ))