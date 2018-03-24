import cv2
import numpy as np

#Importing custom modules
import sql_connector

#Create facedetect object
faceDetect = cv2.CascadeClassifier('haar-cascades/haarcascade_frontalface_default.xml')

#Catpure video from webcam
cam=cv2.VideoCapture(0)

#Insert name into DB and return ID
name=input('Enter name: ')
id = sql_connector.insert(name)

sampleNumber=0

while(True):
    ret, img = cam.read()
    
    #Convert color image to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Detect all faces in frame and returns coordinates
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)
    
    for(x,y,w,h) in faces:
        sampleNumber+=1
        
        #Save face in a folder
        cv2.imwrite("dataset/User."+str(id)+"."+str(sampleNumber)+".jpg", gray[y:y+h, x:x+w])        
        
        #Draw rectangle
        cv2.rectangle (img, (x,y), (x+w, y+h), (0,0,255), 2)
        cv2.waitKey(100)
    
    #Display frame
    cv2.imshow("Face", img)
    cv2.waitKey(1)

    #Only capture 20 images per person
    if(sampleNumber>19):
        break

#Disconnect camera
cam.release()
cv2.destroyAllWindows()