import smbus

class Sensor:
   # i2cBusAddress = 2
    i2c_bus = smbus.SMBus(2)


    def concatenateBytes(self, highByte, lowByte):
        a = highByte << 8
        return (a | lowByte)



