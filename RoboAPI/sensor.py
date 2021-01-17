import smbus


class Sensor:
    
    i2c_bus = smbus.SMBus(2)


    def concatenateBytes(self, high_byte, low_byte):
        a = high_byte << 8
        return a | low_byte



