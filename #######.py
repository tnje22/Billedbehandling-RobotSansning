# import opencv
import cv2
  
# Load the input image
while (cv2.waitKey() !=27):
    image = cv2.imread('fail.png')
    cv2.imshow('windows ', image)
    cv2.moveWindow("windows", 20,20)
    image1 = cv2.imread('fail.png')
    cv2.imshow('Windows ', image1)
    cv2.moveWindow("Windows", 40,20)
    image2 = cv2.imread('fail.png')
    cv2.imshow('vindows ', image2)
    cv2.moveWindow("vindows", 60,20)
    image3 = cv2.imread('fail.png')
    cv2.imshow('Vindows ', image3)
    cv2.moveWindow("Vindows", 80,20)
    cv2.waitKey(0)  
# Window shown waits for any key pressing event
cv2.destroyAllWindows()