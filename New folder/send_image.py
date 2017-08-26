#!/usr/bin/env python
# Import smtplib for the actual sending function
import smtplib
# Import the email modules we'll need
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
# Create a multipart message
import cv2, sys
# Define constants
DEVICE_NUMBER = 0
IMAGE_FILE = “output.jpg”
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
cv2.waitKey(0)
msg = MIMEMultipart()
msg.attach( MIMEText(“Face detected!”) )
msg['Subject'] = “Your DragonBoard 410c has detected someone”
msg['From'] = “linaro@localhost”
msg['To'] = “chayanpathak2011@gmail.com”
# Try opening and attaching the image file
try:
    f = open(“output.jpg”, ”rb”)
    img = MIMEIMAGE( f.read() )
    f.close()
    msg.attach(img)
except IOError:
    print “Error: Cannot find ‘output.jpg’!”
    # Send the message via our own SMTP server (sendmail)
s = smtplib.SMTP('localhost')
s.set_debuglevel(1)
s.sendmail(msg['From'], [msg['To']], msg.as_string())
s.quit()
print "Email sent!"

