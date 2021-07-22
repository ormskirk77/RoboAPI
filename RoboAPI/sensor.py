import smbus


class Sensor:
    
    i2c_bus = smbus.SMBus(2) # I2C bus 2 is used for the esnsors.

    def concatenateBytes(self, high_byte, low_byte):
        '''
        The registers in the ICM20948 are only 8 bit. This function concatenates two registers to give the full 16 bit prescision of a reading.
        :param high_byte:
        :param low_byte:
        :return: 16 bit concatenation of two bytes.
        '''
        a = high_byte << 8
        return a | low_byte



