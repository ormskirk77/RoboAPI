import struct
import mem_registers

from imu import Imu


class Accelerometer(Imu):


    def getRawData(self):
        self.setMemoryBank(0)
        data = self.readContigRegisters(0x2D, 12)
        ax, ay, az, gx, gy, gz = struct.unpack(">hhhhhh", bytearray(data))
        return ax, ay, az, gx, gy, gz

    def getScaledData(self):
        self.setMemoryBank(0)
        data = self.readContigRegisters(0x2D, 12)
        ax, ay, az, gx, gy, gz = struct.unpack(">hhhhhh", bytearray(data))

        self.setMemoryBank(2)
        scale = (self.readSingleRegister(mem_registers.ICM20948_ACCEL_CONFIG) & 0x06) >> 1
      #  self.setMemoryBank(0)
        gs = [16384.0, 8192.0, 4096.0, 2048.0][scale]

        ax /= gs
        ay /= gs
        az /= gs

        return ax, ay, az
