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

    def set_accelerometer_sample_rate(self, rate=125):
        """Set the accelerometer sample rate in Hz."""
        self.setMemoryBank(2)
        # 125Hz - 1.125 kHz / (1 + rate)
        rate = int((1125.0 / rate) - 1)
        # TODO maybe use struct to pack and then write_bytes
        self.write(mem_registers.ICM20948_ACCEL_SMPLRT_DIV_1, (rate >> 8) & 0xff)
        self.write(mem_registers.ICM20948_ACCEL_SMPLRT_DIV_2, rate & 0xff)

    def set_accelerometer_full_scale(self, scale=16):
        """Set the accelerometer fulls cale range to +- the supplied value."""
        self.setMemoryBank(2)
        value = self.readSingleRegister(mem_registers.ICM20948_ACCEL_CONFIG) & 0b11111001
        value |= {2: 0b00, 4: 0b01, 8: 0b10, 16: 0b11}[scale] << 1
        self.write(mem_registers.ICM20948_ACCEL_CONFIG, value)

    def set_accelerometer_low_pass(self, enabled=True, mode=5):
        """Configure the accelerometer low pass filter."""
        self.setMemoryBank(2)
        value = self.readSingleRegister(mem_registers.ICM20948_ACCEL_CONFIG) & 0b10001110
        if enabled:
            value |= 0b1
        value |= (mode & 0x07) << 4
        self.write(mem_registers.ICM20948_ACCEL_CONFIG, value)

    def set_gyro_sample_rate(self, rate=100):
        """Set the gyro sample rate in Hz."""
        self.setMemoryBank(2)
        # 100Hz sample rate - 1.1 kHz / (1 + rate)
        rate = int((1100.0 / rate) - 1)
        self.write(mem_registers.ICM20948_GYRO_SMPLRT_DIV, rate)

    def set_gyro_full_scale(self, scale=250):
        """Set the gyro full scale range to +- supplied value."""
        self.setMemoryBank(2)
        value = self.readSingleRegister(mem_registers.ICM20948_GYRO_CONFIG_1) & 0b11111001
        value |= {250: 0b00, 500: 0b01, 1000: 0b10, 2000: 0b11}[scale] << 1
        self.write(mem_registers.ICM20948_GYRO_CONFIG_1, value)

    def set_gyro_low_pass(self, enabled=True, mode=5):
        """Configure the gyro low pass filter."""
        self.setMemoryBank(2)
        value = self.readSingleRegister(mem_registers.ICM20948_GYRO_CONFIG_1) & 0b10001110
        if enabled:
            value |= 0b1
        value |= (mode & 0x07) << 4
        self.write(mem_registers.ICM20948_GYRO_CONFIG_1, value)