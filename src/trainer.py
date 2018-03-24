import cv2
import numpy as np

#Captures all paths in OS
import os

#PIL is Python Image Library
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
#relative path of the samples
path = 'dataset'

def getImagesWithId(path):
    #Concatenate root path with image name from dataset folder
    #List all directories (pictures in the folder) 
    #Append it to path with the separator
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    IDs = []
    
    for imagePath in imagePaths:        
        #Convert images to grayscale (if not already so)
        faceImg = Image.open(imagePath).convert('L')
        
        #Convert image to numpy array
        faceNp = np.array(faceImg, 'uint8') #OpenCV only works with NUMPY array
        
        #Extract ID from 'dataset\\User1.1.jpg'
        ID = int(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(faceNp)
        IDs.append(ID)
        
        #Display frame
        cv2.imshow("Training", faceNp)
        cv2.waitKey(10)
    
    return np.array(IDs), faces


IDs, faces = getImagesWithId(path)

#Train the recogniser
recognizer.train(faces, IDs)
recognizer.save('recognizer/trainingData.yml')
cv2.destroyAllWindows()