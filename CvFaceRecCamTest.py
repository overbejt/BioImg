import numpy as np
import cv2 as cv

# Get the Haar cascades loaded
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

# Initialize a camera, 0 is usally the web cam
cam = cv.VideoCapture(0)

# Loop until user wants to exit
while(True):
    # Get frame from camera feed
    ret, frame = cam.read()

    # Convert captured from to gray scale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        # Draw rectangles on faces
        img = cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            # Draw rectangles on eyes
            cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    # Display the resulting frame
    cv.imshow('frame', frame)
    # Press q to end the program
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up before closing the program
cam.release()
cv.destroyAllWindows()