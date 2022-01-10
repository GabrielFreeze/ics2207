import cv2
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

cap = cv2.VideoCapture(0)                                                                                         #Capture video from camera
scl = 4                                                                                                           #Scale factor

while cap.isOpened():
    ret, frame = cap.read()                                                                                       #Get current frame.
    
    if ret:
        frame = cv2.flip(frame, 1)                                                                                #Flip the frame horizontally.
        frameSmall = cv2.resize(frame, (0,0), None, 1/scl, 1/scl)                                                 #Resize the frame by a factor of scl.
        frameSmall = cv2.cvtColor(frameSmall, cv2.COLOR_BGR2GRAY)                                                 #Convert to grayscale.
        frameSmall = cv2.equalizeHist(frameSmall)                                                                 #Equalize the histogram.

        try:    face_cascade = cv2.CascadeClassifier(dir_path + '/cascade/haarcascade_frontalface_default.xml')   #Load Face Classifier
        except: face_cascade = cv2.CascadeClassifier(dir_path + '\\cascade\\haarcascade_frontalface_default.xml') #Load Face Classifier

        try:    eye_cascade = cv2.CascadeClassifier(dir_path + '/cascade/haarcascade_eye.xml')                    #Load Eye Classifier
        except: eye_cascade = cv2.CascadeClassifier(dir_path + '\\cascade\\haarcascade_eye.xml')                  #Load Eye Classifier

    
        faces = face_cascade.detectMultiScale(frameSmall, scaleFactor=1.05, minNeighbors=3)                       #Detect faces.
        
        for (x, y, w, h),(xS, yS, wS, hS) in zip([i*scl for i in faces], faces):                                  #For every face detected, get true and scaled coordinates. 
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)                                              #Draw a rectangle around the face.

            roi = frameSmall[yS:yS+hS, xS:xS+wS]                                                                  #Get the bounding box of the face.
            eyes = eye_cascade.detectMultiScale(roi, scaleFactor=1.05, minNeighbors=3)                            #Detect eyes in every face.

            for (ex, ey, ew, eh) in [i*scl for i in eyes]:                                                        #For every eye detected.
                cv2.rectangle(frame, (x+ex, y+ey), (x+ex+ew, y+ey+eh), (0, 255, 0), 2)                            #Draw a rectangle around the eye.
            
        cv2.imshow('frame', frame)                                                                                #Show the camera with the rectangle.
        if cv2.waitKey(1) & 0xFF == ord('q'):                                                                     #Press 'q' to quit.
            break

cap.release()                                                                                                     #Release the camera.
cv2.destroyAllWindows()                                                                                           #Close all windows.

