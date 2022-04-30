import serial.tools.list_ports
import time

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

for the_ports in ports:
    portList.append(str(the_ports))
    print(str(the_ports))

which_port = input("COM")

for i in range(0, len(portList)):
    if portList[i].startswith("COM" + str(which_port)):
        port_var = "COM" + str(which_port)
        print(portList[i])

serialInst.baudrate = 9600
serialInst.port = port_var
serialInst.open()

def write_read(x):
    serialInst.write(bytes(x, 'utf-8'))
    time.sleep(1)


while True:
    num = input()
    write_read(num)
    
