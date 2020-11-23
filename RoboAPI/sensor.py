class Sensor:
    def __init__(self):
        self.i2cBusAddress

    def concatenateBytes(self, byteOne, byteTwo):
        a = byteOne << 8
        a = a | byteTwo
        return a


    pass