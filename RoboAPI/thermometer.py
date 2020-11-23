from RoboAPI.imu import Imu
import smbus


class Thermometer(Imu):

    TEMPERATURE_DEGREES_OFFSET = 18
    TEMPERATURE_SENSITIVITY = 333.87
    ROOM_TEMP_OFFSET = 18

    temperature = None

    def __init__(self):
        self.i2c_bus = smbus.SMBus(2)
        self.temperature = None
        self.updateTemperature()
        pass

    def getTemperature(self):
        if self.temperature == None:
            print("Problem reading temperature")
        elif self.temperature != None:
            return self.temperature

    def updateTemperature(self):
     #   self.i2c_bus.write_byte_data(0x68, 0x06, 0b00000000)
        temp_high = self.i2c_bus.read_byte_data(0x68, 0x39)
        temp_low = self.i2c_bus.read_byte_data(0x68, 0x3A)
        self.temperature = ((self.concatenateBytes(temp_high, temp_low) - self.ROOM_TEMP_OFFSET) /
                            self.TEMPERATURE_SENSITIVITY) + self.TEMPERATURE_DEGREES_OFFSET

