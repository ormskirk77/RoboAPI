from ICM20948 import ICM20948
from RoboAPI.robo import Robo


robo = Robo()

print("Temp: " + str(robo.thermometer.getTemperature()))

imu = ICM20948()

temp = imu.read_temperature()
print("Temp: " + str(temp) + "\n")