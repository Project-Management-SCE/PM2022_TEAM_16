import os
from PIL import Image
import numpy as np
import cv2 
import pickle
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

image_dir = os.path.join(BASE_DIR, "images")
face_cascade = cv2.CascadeClassifier('C:\\Users\\kevyn\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create() 

y_labels = []
x_train = []
current_id = 0
label_ids = {}
for root,dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("jpg") or file.endswith("png") or file.endswith("jpeg"):
            path= os.path.join(root,file)
            label = os.path.basename(os.path.dirname(path)).replace(" ","-").lower()
            #-------------------------------------------------IMAGE ''PREPROCESSING''------------------------------------------------------------------------------
            if label in label_ids:
                pass
            else : 
                label_ids[label] = current_id
                current_id += 1 
            id_ = label_ids[label]    
            print(label_ids)
            #y_labels.append(label)
            #x_train.append(path)
            pil_image = Image.open(path).convert("L") # gray scaling
            size=(300,300)
            final_image = pil_image.resize(size, Image.ANTIALIAS) #resizing image
            image_array = np.array(final_image, "uint8") # converti limage en matrice
           # print(image_array)
            faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5,minNeighbors=3)

            for (x,y,w,h) in faces :
                roi = image_array[y:y+h ,x:x+w]
                x_train.append(roi)
                y_labels.append(id_)


            #===============================================================================================================================================#
#print(y_labels)
#print(x_train)

with open("labels.pickle", "wb") as f :
    pickle.dump(label_ids, f)

#creating training model

recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainner.yml")