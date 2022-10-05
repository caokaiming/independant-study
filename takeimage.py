import numpy as np
import cv2

print('Starting two Cameras. Press and maintain the space bar to exit the script\n')

id_image=27326
counter = 0
# termination criteria
criteria =(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Call the two cameras
CamL= cv2.VideoCapture(0)   # 0 -> Left Camera
CamR= cv2.VideoCapture(1)   # 1 -> Right Camera
path = "D:/images/mav0/V101.txt"
f = open(path, 'w')
x = 0 
while True:
    retR, frameR= CamR.read()
    retL, frameL= CamL.read()
    grayR= cv2.cvtColor(frameR,cv2.COLOR_BGR2GRAY)
    grayL= cv2.cvtColor(frameL,cv2.COLOR_BGR2GRAY)

    cv2.imshow('imgR',frameR)     
    cv2.imshow('imgL',frameL)

    str_id_image= str(id_image)
    ##print('Images ' + t + ' saved for right and left cameras')
    if (counter % 2 == 0):
        cv2.imwrite('D:\images\mav0\cam0\data\\1403715'+str_id_image+'2142976.png',frameR) # Save the image in the file where this Programm is located
        cv2.imwrite('D:\images\mav0\cam1\data\\1403715'+str_id_image+'2142976.png',frameL)
        f.write('1403715'+str_id_image+'2142976\n')
        print("image saved scuess!")
    elif (counter % 2 == 1):
        cv2.imwrite('D:\images\mav0\cam0\data\\1403715'+str_id_image+'2143104.png',frameR) # Save the image in the file where this Programm is located
        cv2.imwrite('D:\images\mav0\cam1\data\\1403715'+str_id_image+'2143104.png',frameL)
        f.write('1403715'+str_id_image+'2143104\n')
        print("image saved scuess!")
    id_image = id_image + 5
    counter += 1 
    for i in range(10):
        x += 1
    x = 0
    # End the Programme
    if cv2.waitKey(1) & 0xFF == ord(' '):   # Push the space bar and maintan to exit this Programm
        break

# Release the Cameras
CamR.release()
CamL.release()
cv2.destroyAllWindows()    
