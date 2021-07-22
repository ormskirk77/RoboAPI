from ICM20948 import ICM20948
from RoboAPI.robo import Robo
from direction import Direction
import os
import time

'''
Test script to check aspects fo the RoboAPI are working as expected. NOT part of the main API but should function as 
a set of examples for others to follow. 
'''

robo = Robo()
print("Starting...")

#========================== SERVO TESTING ==============================
robo.set_servo_position(3, 60)
print("pwm set to 30")
time.sleep(10)
# robo.set_servo_position(3, 90)
# print("pwm set to 90")
# time.sleep(10)
# robo.set_servo_position(3, 100)
# print("pwm set to 100")
# time.sleep(10)
# robo.set_servo_position(3, 180)
# print("pwm set to 180")
# time.sleep(10)

# ==================== MOTOR TESTING ======================================

# robo.set_motor_direction(3, Direction.BRAKE)
# time.sleep(2)
#
# print("On")
# robo.set_motor_direction(3, Direction.FORWARD)
# # TODO Make sure the PWM is correct and the speed works for both motors.
# for i in range(1, 11):
#     robo.set_motor_speed(3, i*10)
#     time.sleep(0.5)
#     print("speed: " + str(robo.motor1.speed) + "     i: " + str(i))
#
# time.sleep(2)
#
# robo.set_motor_direction(3, Direction.BACKWARD)
# print("Changed direction")
# time.sleep(2)
#
# robo.set_motor_direction(1, Direction.FORWARD)
# print("Spin")
# time.sleep(3)
#
# robo.set_motor_direction(1, Direction.BACKWARD)
# robo.set_motor_direction(2, Direction.FORWARD)
# print("Spin")
# time.sleep(2)
# #robo.set_motor_direction(2, Direction.BACKWARD)
# #time.sleep(10)
#
# robo.motor1.motor_off()
# robo.motor2.motor_off()
# print("Stopped")


#======================= SENSOR TESTING ========================================
#robo.initialiseImu()
# print("Temp: " + str(robo.thermometer.getTemperature()))
# print("Accel: " + str(robo.accelerometer.getScaledData()))

# imu = ICM20948()
# #
# # temp = imu.read_temperature()
# # print("Temp: " + str(temp) + "\n")
#
# # full scale is +/- 250
# # imu.set_gyro_full_scale()
# while 1:
#     x, y, z = imu.read_magnetometer_data()
#     ax, ay, az, gx, gy, gz = imu.read_accelerometer_gyro_data()
#
#     # print("""
#     # Accel: {:05.2f} {:05.2f} {:05.2f}
#     # Gyro:  {:05.2f} {:05.2f} {:05.2f}
#     # Mag:   {:05.2f} {:05.2f} {:05.2f}""".format(
#     #     ax, ay, az, gx, gy, gz, x, y, z
#     # ))
#     print("""
#     Gyro:  {:05.2f} {:05.2f} {:05.2f}""".format(
#         gx, gy, gz
#     ))
#     time.sleep(1)