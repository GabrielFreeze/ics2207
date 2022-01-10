import cv2
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))
scl = 1


for i in range(1,13):    
    name = f'\\validation-set\\test ({i}).jpg'
    img = cv2.imread(dir_path + name)
    cv2.imshow(name, img)
    img = cv2.flip(img, 1)                                                          
    imgSmall = cv2.resize(img, (0,0), None, 1/scl, 1/scl)                           
    imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2GRAY)                           
    imgSmall = cv2.equalizeHist(imgSmall)

    try: face_cascade = cv2.CascadeClassifier(dir_path + '/cascade/cascade.xml')        
    except: face_cascade = cv2.CascadeClassifier(dir_path + '\\cascade\\cascade.xml')   
    faces = face_cascade.detectMultiScale(imgSmall, scaleFactor=1.05, minNeighbors=3) 
    
    for (x, y, w, h) in [i*scl for i in faces]:                                         
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    cv2.imshow(name, img)                                                          


while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):                                               
        break

