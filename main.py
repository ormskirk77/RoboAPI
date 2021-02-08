from ICM20948 import ICM20948
from RoboAPI.robo import Robo
from direction import Direction
import os
import time

print(os.getcwd())
robo = Robo()

# robo.set_servo1_position(30)
# print("pwm set to 30")
# time.sleep(10)
# robo.set_servo1_position(90)
# print("pwm set to 90")
# time.sleep(10)
# robo.set_servo1_position(100)
# print("pwm set to 100")
# time.sleep(10)
# robo.set_servo1_position(180)
# print("pwm set to 180")
# time.sleep(10)
# robo.set_servo1_position(0)
# time.sleep(1)
robo.initialiseImu()

# robo.set_motor1_direction(Direction.FORWARD)
# robo.set_motor1_speed(70)
# time.sleep(5)
# robo.set_motor1_direction(Direction.BACKWARD)
# time.sleep(5)
# robo.set_motor1_direction(Direction.BRAKE)
# robo.motor1.motor_off()

# print("Temp: " + str(robo.thermometer.getTemperature()))
# print("Accel: " + str(robo.accelerometer.getScaledData()))

imu = ICM20948()
#
# temp = imu.read_temperature()
# print("Temp: " + str(temp) + "\n")

# full scale is +/- 250
# imu.set_gyro_full_scale()
while 1:
    x, y, z = imu.read_magnetometer_data()
    ax, ay, az, gx, gy, gz = imu.read_accelerometer_gyro_data()

    # print("""
    # Accel: {:05.2f} {:05.2f} {:05.2f}
    # Gyro:  {:05.2f} {:05.2f} {:05.2f}
    # Mag:   {:05.2f} {:05.2f} {:05.2f}""".format(
    #     ax, ay, az, gx, gy, gz, x, y, z
    # ))
    print("""
    Gyro:  {:05.2f} {:05.2f} {:05.2f}""".format(
        gx, gy, gz
    ))
    time.sleep(1)