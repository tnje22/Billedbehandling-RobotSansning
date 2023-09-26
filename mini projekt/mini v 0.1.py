# import opencv
import cv2
image = cv2.imread('King Domino dataset\Cropped and perspective corrected boards\1.jpg')
cv2.imshow('Plade', image)
cv2.waitKey(0)  
cv2.destroyAllWindows()