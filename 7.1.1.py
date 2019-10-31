import cv2
import subprocess
subprocess.call("raspistill -n -t 250 -o 7.1.1.jpg", shell=True)

img = cv2.imread("7.1.1.jpg")
cv2.imshow('dst', img)
