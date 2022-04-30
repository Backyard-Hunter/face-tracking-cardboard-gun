from pyfirmata import Arduino, SERVO, util
from time import sleep

port = 'COM4'
pin1 = 10
pin2 = 9
board = pyfirmata.Arduino(port)
servo1 = board.get_pin('d:9:s')
servo2 = board.get_pin('d:10:s')

for angle in range(90, 180, 1):
    servo1.write(angle)
    time.sleep(0.015)

for angle in range(180, 90, -1):
    servo2.write(angle)
    time.sleep(0.015)