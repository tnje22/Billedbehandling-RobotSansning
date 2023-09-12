import cv2
import imutils

frame = cv2.imread('image.jpg')
frame = imutils.resize(frame, width=800, height=480)

cv2.putText(frame, "Some information", (5, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 1)
cv2.putText(frame, "More information", (5, 60), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 1)
cv2.putText(frame, "Some more information", (5, 90), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 1)

cv2.imshow('Application', frame)
key = cv2.waitKey(0)