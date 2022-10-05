import numpy as np
import cv2
print("Starting Check two camera....")

CamL= cv2.VideoCapture(0)   # 0 -> Left Camera
#CamR= cv2.VideoCapture(1)   # 1 -> Right Camera

while True:
    #retR, frameR= CamR.read()
    retL, frameL= CamL.read()
    #grayR= cv2.cvtColor(frameR,cv2.COLOR_BGR2GRAY)
    grayL= cv2.cvtColor(frameL,cv2.COLOR_BGR2GRAY)

    #cv2.imshow('imgR',frameR)     
    cv2.imshow('imgL',frameL)

    if cv2.waitKey(1) & 0xFF == ord(' '):   # Push the space bar and maintan to exit this Programm
        break

#CamR.release()
CamL.release()
cv2.destroyAllWindows()    