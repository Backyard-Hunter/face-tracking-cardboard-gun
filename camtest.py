import cv2
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

imcap = cv2.VideoCapture(0) # use shitty webcam camera
imcap.set(3, 640) # width 640
imcap.set(4, 640) # height 480

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") # use pretrained viola-jones algorithm
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
thickness = 2
color = (0, 255, 0)






def write_read(x,y):
    serialInst.write(bytes(f'X{x} Y{y}', 'utf-8'))

    time.sleep(1)

def servo_move(x,y,w,h):
    mynose_x = (x + w)/2
    mynose_y = (y + h)/2
    adjusted_mynose_x = mynose_x / (640/180)
    adjusted_mynose_y = mynose_y / (640/180)
    
    write_read(adjusted_mynose_x, adjusted_mynose_y)

    print(adjusted_mynose_x)
    print(adjusted_mynose_y)
    time.sleep(1)


    

while True:
    success, img = imcap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert image to grayscale

    faces = face_cascade.detectMultiScale(imgGray, 1.3, 5) # get corners around the face, set scale to 1.3 and set max number of neighbours to be detected to 5

    for(x,y,w,h) in faces:
        img = cv2.rectangle(img, (x,y), (x + w, y + h), (0, 255,0), 3) # draw a rectangle around face to make you look like a clown
        servo_move(x,y,w,h)

    cv2.imshow('face_detect', img) # show the now new image with the rectangles drawn in it

    if cv2.waitKey(10) & 0xFF == ord('l'): # exit when pressed L, because computer is salty
        break

cap.release()
cv2.destroyWindow('face_detect') # close window

