import cv2
import numpy as np

#Custom imports
from src import dataset_creator
from src import trainer
from src import sql_connector

#Create facedetect object
faceDetect = cv2.CascadeClassifier('haar-cascades/haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

#Create recognizer
rec = cv2.face.LBPHFaceRecognizer_create()

#Load trained recogniser
rec.read("recognizer/trainingData.yml")
ID=0

while(True):
    #Get frame and cvt colour
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Detect faces
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)
    
    for(x,y,w,h) in faces:
        #Draw around face
        cv2.rectangle (img, (x,y), (x+w, y+h), (0,0,255), 2)

        #Recognises the face in rectangle
        ID, conf = rec.predict(gray[y:y+h, x:x+w])

        #Retrieves name from database and prints it at (x, y+h) 
        name = sql_connector.retrieve(ID)
        cv2.putText(img, name, (x,y+h), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255))         
    
    #Display frame
    cv2.imshow("Face", img)

    #Quit frame as needed
    if(cv2.waitKey(1)==ord('q')):
        break

#Disconnect
cam.release()
cv2.destroyAllWindows()