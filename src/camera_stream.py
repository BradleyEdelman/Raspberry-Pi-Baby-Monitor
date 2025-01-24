import cv2
import numpy as np

# OpenCV video capture object for the camera
cap = cv2.VideoCapture(0)

# Set the width and height of the video stream (optional)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale (optional, depending on use case)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the frame (only when display is attached)
    # cv2.imshow("Video Stream", gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
