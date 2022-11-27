import cv2

# Load the cascade
trained_face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

# To use a video file as input
video = cv2.VideoCapture('bw.mp4')


while True:
    # Read the frame
    _, img = video.read()
    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 100, 255, cv2.THRESH_BINARY)
    cv2.imshow('Black white image', blackAndWhiteImage)
    colored = grayImage = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    cv2.imshow('Colored image', colored)
    # cv2.imshow('Gray image', grayImage)
    # # Convert to grayscale
    # #gray_scaled_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()