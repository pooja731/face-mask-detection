
import cv2

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

'''Eye detect using Eye Cascade'''
eyedetect = cv2.CascadeClassifier('haarcascade_eye.xml')



'''creating a video capture object.
    Value is 0 because we are using primary camera that is webacm.
    If there is a need to use the secondary camera we can change the value from 0 to 1'''
video = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))


#loop until python is able to read the video object
while True:

    '''>check is a bool data type(Just like true and false), return true if python is able to read the video capture object.
        >frame is a numpy array, it represents the first image that video captures '''
    check, frame = video.read()

    # converting the image into a gray scale image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # search the coordinates of the face in the image
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)

    '''Method to create face rectangle.
        consist of image object that is "frame", RGB value of the rectangle outine and width of the rectangle'''
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)

        '''Method to create face rectangle.'''
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # search the coordinates of the eyes in the image
        eyes = eyedetect.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 5)

    #cv2.imshow() to display an image in a window
    cv2.imshow('Face', frame)

    '''generate a new frame after every 1 miliseconds since we know that a video is nothing but multiple 
        frames that are displayed quickly'''
    out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
out.release()
cv2.destroyAllWindows()
