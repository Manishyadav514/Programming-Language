import cv2

# Will load pre-trained data from open Cv using haar cascade algorithm
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#select image to read
image = cv2.imread('faces.jpg')
#image = cv2.resize(image, (960, 620))
cv2.imshow("colored-image",image)       # to show your image

# change the colored image into black and white
grayscaled_image =cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("grayscaled-image",grayscaled_image)

# Detect the faces
faces = trained_face_data.detectMultiScale(grayscaled_image)
# Draw the rectangle around each face
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # Display
    cv2.imshow('face-captured', image)

cv2.waitKey(0)





