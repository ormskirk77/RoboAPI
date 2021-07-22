import mem_registers
from imu import Imu

'''
The thermometer sensor is packaged in the IMU20948 chip. See datasheet for the conversion formula. 
'''
class Thermometer(Imu):
    # Constants with assumptions such as the ambient room temperature.
    TEMPERATURE_DEGREES_OFFSET = mem_registers.ICM20948_TEMPERATURE_DEGREES_OFFSET
    TEMPERATURE_SENSITIVITY = mem_registers.ICM20948_TEMPERATURE_SENSITIVITY
    ROOM_TEMP_OFFSET = mem_registers.ICM20948_ROOM_TEMP_OFFSET

    _temperature = None

    def getTemperature(self):
        '''
        Returns the current temperature based on the hardcoded constants in thermometer.py.
        :return: Temperature in degrees Celsius
        '''
        self._updateTemperature()
        if self._temperature is None:
            print("Problem reading temperature.\n")
        elif self._temperature is not None:
            return self._temperature

    def _updateTemperature(self):
        '''
        Updates the RoboAPI instances temperature with the current reading.
        :return: nothing
        '''
        self.setMemoryBank(0)
        temp_high = self.readSingleRegister(mem_registers.ICM20948_TEMP_OUT_H)
        temp_low = self.readSingleRegister(mem_registers.ICM20948_TEMP_OUT_L)

        print("temp High: " + str(temp_high) + "   " + "temp low: " + str(temp_low))
        temp_bytes = self.concatenateBytes(temp_high, temp_low)
        self._temperature = ((temp_bytes - self.ROOM_TEMP_OFFSET) / self.TEMPERATURE_SENSITIVITY) + self.TEMPERATURE_DEGREES_OFFSET

