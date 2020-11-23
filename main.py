import socket
import mraa


from RoboAPI.robo import Robo

robo = Robo()
print(robo.thermometer.getTemperature())

print(socket.gethostname())

