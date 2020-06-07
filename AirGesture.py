import cv2
import numpy as np
import time
from find_loc_uncompiled import *
from SwipePosition_uncompiled import *
cap = cv2.VideoCapture(0)
loc = Locate()
key = KeyBD()

oldX, oldY = -1, -1
lower_red = np.array([30,150,50])
upper_red = np.array([180, 255, 255])
    

while True :
    _, frame = cap.read()
    frame = cv2.resize(frame, (200, 200))
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    kernel = np.ones((5,5),np.uint8)
    
    dilation = cv2.dilate(mask,kernel,iterations = 1)

    cv2.namedWindow('Dilation',cv2.WINDOW_NORMAL)
    
    cv2.imshow('Original',frame)
    cv2.imshow('Dilation',dilation)


    analytic = np.asarray(dilation)
    x, y = loc.find(analytic)
    if x == -1 :
        pass
    elif oldX > x :
        print('r', end='')
        key.press('r')
        key.press('r')
        
    elif oldX < x :
        print('l', end='')
        key.press('l')
        key.press('l')
    

    '''
    if y == -1 :
        pass
    elif oldY > y :
        key.press('u')
    elif oldY < y :
        key.press('d')
    '''
    
    
    oldX, oldY = x, y
    
    
    if cv2.waitKey(1) & 0xff == ord('q') :
          print("pressed quit")
          break

cap.release()
cv2.destroyAllWindows()
