import cv2
import os
import numpy as np
import PIL

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, 'images')

trained_face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

label_ids = {}
y_labels = []
x_train = []
current_id = 0

for root, dir, files in os.walk(IMAGE_DIR):
    #print(root, dir, files) # files = all files in the directory
    for file in files:
        path = os.path.join(root, file)
        label = os.path.basename(root).lower()
        #print(path, label)

        if label not in label_ids:
            label_ids[label] = current_id
            current_id +=1
        id_ = label_ids[label]
        print(label_ids)

        #pil_image = Image.open(path).convert("L")
        #image_array = np.array(pil_image, 'unit8')
        #print(image_array)
        an_image = PIL.Image.open("example_image.png")
        image_sequence = an_image.getdata()
        image_array = np.array(image_sequence)

        print(image_array)