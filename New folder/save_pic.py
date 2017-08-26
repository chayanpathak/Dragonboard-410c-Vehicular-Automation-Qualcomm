#!/usr/bin/env python
import cv2, sys
# Define constants
DEVICE_NUMBER = 0
IMAGE_FILE = "output.jpg"
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
# Save the frame as an image file
cv2.imwrite(IMAGE_FILE, frame)
# Read the output file
img = cv2.imread(IMAGE_FILE)
# Show the saved image on the screen
cv2.imshow("DragonBoard 410c Workshop", img)
# Exit program after waiting indefinitely for a pressed key
cv2.waitKey(0)
