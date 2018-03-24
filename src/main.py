"""
@author: Shreyas Parbat

Detect recorded face and authorises app to show data
"""

import cv2

#Importing custom modules
from src import sql_connector

def authorise():

    #Boolean to decide wether authorised face or not
    isAuthorised = False

    #Import cascade and set up video feed
    face_cascade = cv2.CascadeClassifier('haar-cascades/haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)

    #Create recognizer and load training data file
    rec = cv2.face.LBPHFaceRecognizer_create()
    rec.read("src/recognizer/trainingData.yml")

    while True:
        #Get frame and cvt colour
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        #Detect faces and log in console
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        print (faces)
    
        for (x, y, w, h) in faces:
            #Draw around face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            #Recognises the face in rectangle
            ID, conf = rec.predict(gray[y:y+h, x:x+w])

            #Retrieves name from database and prints it at (x, y+h)
            name = sql_connector.retrieve(ID)
            cv2.putText(frame, name, (x,y+h), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255))

            #Authorise if authorised person
            if name == "Shubham":
                isAuthorised = True

        #Display frame
        cv2.imshow('frame', frame)
    
        #Quit frame as needed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    #Disconnect
    cv2.destroyAllWindows()
    cap.release()

    #Return authorisation status
    return isAuthorised