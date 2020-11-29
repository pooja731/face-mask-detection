import cv2
import os
#http://alereimondo.no-ip.org/OpenCV/34/
cascPath = os.path.dirname(
    cv2.__file__) + "/data/haarcascade_frontalface_alt2.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

datasets = 'datasets'  
  
  
# These are sub data sets of folder,  
# for my faces I've used my name you can  
# change the label here 
sub_data = 'POOJA'     
  
path = os.path.join(datasets, sub_data) 
if not os.path.isdir(path): 
    os.mkdir(path) 
  
# defining the size of images  
(width, height) = (400, 500)

video_capture = cv2.VideoCapture(0)
count = 1
while count < 30:  
    (_, img) = video_capture.read() 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    faces = faceCascade.detectMultiScale(gray, 1.3, 4) 
    for (x, y, w, h) in faces: 
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2) 
        face = gray[y:y + h, x:x + w] 
        face_resize = cv2.resize(face, (width, height)) 
        cv2.imwrite('% s/% s.png' % (path, count), face_resize) 
    count += 1       
    cv2.imshow('OpenCV', img) 
    key = cv2.waitKey(100) & 0xff  
    if key == 27: 
        break
    elif count >= 30: # Take 30 face sample and stop video
        break
   # video_capture.release()
   #cv2.destroyAllwindows()
#