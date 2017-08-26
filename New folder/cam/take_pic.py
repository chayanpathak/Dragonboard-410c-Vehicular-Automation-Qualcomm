#!/usr/bin/env python
import cv2, sys
# Define constants
DEVICE_NUMBER = 0
# Initialize webcam
vc = cv2.VideoCapture(DEVICE_NUMBER)
# Check if the webcam works
if vc.isOpened():
 # Try to get the first frame
 retval, frame = vc.read()
else:
 # Exit the program
 sys.exit(1)
# Read in the next frame
retval, frame = vc.read()
# Show the frame to the user
cv2.imshow("DragonBoard 410c Workshop", frame)
# Exit program after waiting indefinitely for a pressed key
cv2.waitKey(0)
