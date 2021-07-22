from sensor import Sensor
import mem_registers
import time


class Imu(Sensor):
    _memoryBank = -1

    def initialiseIMU(self):
        '''
        The IMU needs to be initialsed after power-up, otherwise all the sensors will remain in a 'sleep' state to conserve power.
        :return: Nothing
        '''
        print("imu")

        self.setMemoryBank(0)
        if not self.readSingleRegister(mem_registers.ICM20948_WHO_AM_I) == mem_registers.CHIP_ID:
            raise RuntimeError("Unable to find ICM20948")

        self.write(mem_registers.ICM20948_PWR_MGMT_1, 0x80)
        time.sleep(0.01)
        self.write(mem_registers.ICM20948_PWR_MGMT_1, 0x01)
        self.write(mem_registers.ICM20948_PWR_MGMT_2, 0x00)

        self.setMemoryBank(2)
        self.write(mem_registers.ICM20948_INT_PIN_CFG, 0x30)

        self.setMemoryBank(3)
        self.write(mem_registers.ICM20948_I2C_MST_CTRL, 0x4D)
        self.write(mem_registers.ICM20948_I2C_MST_DELAY_CTRL, 0x01)

    def setMemoryBank(self, memory_bank):
        '''
        Sets the register so when you call a write function it writes to the correct memory bank on the IMU20948
        :param memory_bank: memory bank number
        :return: nothing
        '''
        if not self._memoryBank == memory_bank:
            self.write(mem_registers.ICM20948_BANK_SEL, memory_bank << 4)
            self._memoryBank = memory_bank

    def readSingleRegister(self, register_address):
        '''
        Reads a single register of the given address. Be sure to check you are in the correct memory bank BEFORE
        calling this function.
        :param register_address: address to be read
        :return:
        '''
        return self.i2c_bus.read_byte_data(mem_registers.I2C_ADDR, register_address)

    def readContigRegisters(self, start_address, num_of_bytes=1):
        """
        Read several register in one read.
        :param start_address:
        :param num_of_bytes:
        :return:
        """
        return self.i2c_bus.read_i2c_block_data(mem_registers.I2C_ADDR, start_address, num_of_bytes)

    def write(self, reg, value):
        """Write byte to the sensor."""
        self.i2c_bus.write_byte_data(mem_registers.I2C_ADDR, reg, value)
        time.sleep(0.0001)

