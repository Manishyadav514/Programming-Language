import cv2

# Load the cascade
trained_face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

# To capture video from webcam.
video = cv2.VideoCapture(0)

# To use a video file as input
#video = cv2.VideoCapture('kid.mp4')


while True:
    # Read the frame
    _, img = video.read()
    # Convert to grayscale
    gray_scaled_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = trained_face_cascade.detectMultiScale(gray_scaled_image)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # Display
    cv2.imshow('captured-image', img)
    # Stop if escape key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object
video.release()

# Destroy all the windows
cv2.destroyAllWindows()