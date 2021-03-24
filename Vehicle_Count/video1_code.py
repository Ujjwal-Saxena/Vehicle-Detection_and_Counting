# FOR VIDEO 1


import cv2
import numpy as np
from time import sleep

lat_min=68
alt_min=68 
offset=3.5 
pos_line=270 
delay= 60 

detect = []
count= 0

	
def position_control(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx,cy

cap = cv2.VideoCapture('C:/Users/Lenovo/Downloads/Vehicle_Count/video1.mp4')
subtractor = cv2.bgsegm.createBackgroundSubtractorMOG()

while True:
    ret , frame1 = cap.read()
    tempo = float(1/delay)
    sleep(tempo) 
    grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey,(3,3),2)
    img_sub = subtractor.apply(blur)
    dilate = cv2.dilate(img_sub,np.ones((5,5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilater = cv2.morphologyEx (dilate, cv2. MORPH_CLOSE , kernel)
    contourn,h=cv2.findContours(dilater,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.imshow("Blur Image",blur)
    cv2.imshow("Subtractor image",img_sub)
    cv2.imshow("Kernel Image",kernel)
    # cv2.imshow("Contourn",contourn)


    cv2.line(frame1, (500, pos_line), (1400, pos_line), (255,127,0), 4) 
    for(i,c) in enumerate(contourn):
        (x,y,w,h) = cv2.boundingRect(c)
        validar_contourn = (w >= lat_min) and (h >= alt_min)
        if not validar_contourn:
            continue

        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),4)        
        center = position_control(x, y, w, h)
        detect.append(center)
        cv2.circle(frame1, center, 4, (0, 0,255), -1)

        for (x,y) in detect:
            if y<(pos_line+offset) and y>(pos_line-offset):
                
                cv2.line(frame1, (500, pos_line), (1400, pos_line), (0,127,255), 3)  
                count+=1
                detect.remove((x,y))
                print("car is detected : "+str(count))        
       
    cv2.putText(frame1, "VEHICLE COUNT : "+str(count), (300, 115), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),5)
    cv2.imshow("Video Original" , frame1)
    cv2.imshow("Detecter",dilater)

    if cv2.waitKey(1) == ord('q'):
        break
    
cv2.destroyAllWindows()
cap.release()
