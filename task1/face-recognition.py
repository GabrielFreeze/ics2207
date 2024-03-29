import cv2
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))
cap = cv2.VideoCapture(0)
scl = 4

while cap.isOpened():
    ret, frame = cap.read()                                                                 # Get current frame.
    
    if ret:
        frame = cv2.flip(frame, 1)                                                          #Flip the frame horizontally.
        frameSmall = cv2.resize(frame, (0,0), None, 1/scl, 1/scl)                           #Resize the frame by a factor of scl.
        frameSmall = cv2.cvtColor(frameSmall, cv2.COLOR_BGR2GRAY)                           #Convert to grayscale.
        frameSmall = cv2.equalizeHist(frameSmall)                                           #Equalize the histogram.

        try: face_cascade = cv2.CascadeClassifier(dir_path + '/cascade/cascade.xml')        #Load the cascade (Linux).
        except: face_cascade = cv2.CascadeClassifier(dir_path + '\\cascade\\cascade.xml')   #Load the cascade (Windows).
        faces = face_cascade.detectMultiScale(frameSmall, scaleFactor=1.05, minNeighbors=3) #Detect faces.
        
        for (x, y, w, h) in [i*scl for i in faces]:                                         #Draw rectangle around the faces.
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        cv2.imshow('frame', frame)                                                          #Show the camera with the rectangle.
        
        if cv2.waitKey(1) & 0xFF == ord('q'):                                               #Press 'q' to quit.
            break

