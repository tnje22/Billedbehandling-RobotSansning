# import opencv

import cv2
x = 1
y = 1

cv2.namedWindow("windows")
# Load the input image
while (cv2.waitKey() !=27):
    cv2.waitKey(0)
    cv2.moveWindow("windows", 1200,700)
    cv2.waitKey(0)
    cv2.moveWindow("windows", 200,200)
    cv2.waitKey(0)
    cv2.moveWindow("windows", 200,700)
    cv2.waitKey(0)
    cv2.moveWindow("windows", 1200,200)
# Window shown waits for any key pressing event
cv2.destroyAllWindows()