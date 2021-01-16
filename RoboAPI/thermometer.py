import mem_registers
from imu import Imu


class Thermometer(Imu):

    TEMPERATURE_DEGREES_OFFSET = 21
    TEMPERATURE_SENSITIVITY = 333.87
    ROOM_TEMP_OFFSET = 21

    _temperature = None

    def getTemperature(self):
        self._updateTemperature()
        if self._temperature is None:
            print("Problem reading temperature.\n")
        elif self._temperature is not None:
            return self._temperature

    def _updateTemperature(self):
        self.setMemoryBank(0)
        temp_high = self.imu.readSingleRegister(mem_registers.ICM20948_TEMP_OUT_H)
        temp_low = self.imu.readSingleRegister(mem_registers.ICM20948_TEMP_OUT_L)

        print("temp High: " + str(temp_high) + "   " + "temp low: " + str(temp_low))

        self._temperature = ((self.concatenateBytes(temp_high, temp_low) - self.ROOM_TEMP_OFFSET) /
                             self.TEMPERATURE_SENSITIVITY) + self.TEMPERATURE_DEGREES_OFFSET

