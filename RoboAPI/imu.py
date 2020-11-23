from RoboAPI.sensor import Sensor
import RoboAPI.mem_registers


class Imu(Sensor):

    def __init__(self):
        self.i2cBusAddress = 2
        self._memoryBank = None

    def setMemoryBank(self, memoryBank):
        if not self._memoryBank == memoryBank:
            self.write(RoboAPI.mem_registers.ICM20948_BANK_SEL, memoryBank << 4)
            self._memoryBank = memoryBank


