import cv2
import os
#http://alereimondo.no-ip.org/OpenCV/34/
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye-cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')

video_capture = cv2.VideoCapture(0)

while 1:  
    (_, img) = video_capture.read() 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    faces = faceCascade.detectMultiScale(gray, 1.3, 5) 
    for (x, y, w, h) in faces: 
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2) 
        face_gray = gray[y:y + h, x:x + w]
        face_color = img[y:y + h, x:x + w]

eyes = eye-cascade.detectmultiscale(face) 
for (ex,ey,e,eh) in eyes: 
    cv2.rectangle(face_color,(ex,ey),(ex,+ew,ey+eh),(0,233,1,2))        
        
    cv2.imshow('img', img) 
    key = cv2.waitKey(30) & 0xff  
    if key == 27: 
        break
   # elif count >= 30: # Take 30 face sample and stop video
     #   break
   # video_capture.release()
   #cv2.destroyAllwindows()
#