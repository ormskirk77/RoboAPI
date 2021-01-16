from sensor import Sensor
import mem_registers, time
from smbus import SMBus


class Imu(Sensor):


    def initialiseIMU(self):

        print("imu")
        self._memoryBank = -1

        self.setMemoryBank(0)
        if not self.readSingleRegister(mem_registers.ICM20948_WHO_AM_I) == mem_registers.CHIP_ID:
            raise RuntimeError("Unable to find ICM20948")


        self.write(mem_registers.ICM20948_PWR_MGMT_1, 0x80)
        time.sleep(0.01)
        self.write(mem_registers.ICM20948_PWR_MGMT_1, 0x01)
        self.write(mem_registers.ICM20948_PWR_MGMT_2, 0x00)

        self.setMemoryBank(2)
        self.set_gyro_sample_rate(100)
        self.set_gyro_low_pass(enabled=True, mode=5)
        self.set_gyro_full_scale(250)

        self.set_accelerometer_sample_rate(125)
        self.set_accelerometer_low_pass(enabled=True, mode=5)
        self.set_accelerometer_full_scale(16)
        self.write(mem_registers.ICM20948_INT_PIN_CFG, 0x30)

        self.setMemoryBank(3)
        self.write(mem_registers.ICM20948_I2C_MST_CTRL, 0x4D)
        self.write(mem_registers.ICM20948_I2C_MST_DELAY_CTRL, 0x01)




    def setMemoryBank(self, memoryBank):
        if not self._memoryBank == memoryBank:
            self.write(mem_registers.ICM20948_BANK_SEL, memoryBank << 4)
            self._memoryBank = memoryBank


    def readSingleRegister(self, registerAddress):
        return self.i2c_bus.read_byte_data(mem_registers.I2C_ADDR, registerAddress)

    def readContigRegisters(self, startAddress, numOfBytes=1):
        return self.i2c_bus.read_i2c_block_data(mem_registers.I2C_ADDR, startAddress, numOfBytes)

    def write(self, reg, value):
        """Write byte to the sensor."""
        self.sensor.i2c_bus.write_byte_data(mem_registers.I2C_ADDR, reg, value)
        time.sleep(0.0001)

