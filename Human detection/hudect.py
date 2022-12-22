import cv2
import numpy as np
import serial
import time
    
arduino = serial.Serial(port='COM5', baudrate=9600, timeout=.1)
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

human = cv2.HOGDescriptor()
human.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cv2.startWindowThread()

vidCap = cv2.VideoCapture(0)

# out = cv2.VideoWriter(
#     'output.avi',
# )

while True:
    ret,frame = vidCap.read()
    frame = cv2.resize(frame,(640,480))
    greay = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)

    boxes, weight = human.detectMultiScale(frame, winStride =(8,8))
    boxes = np.array([[x,y,x+w,y+h] for (x,y,w,h) in boxes])
    for (xA,yA,xB,yB) in boxes:
        cv2.rectangle(frame,(xA,yA),(xB,yB),(255,0,0),2)

    cv2.imshow('video',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break