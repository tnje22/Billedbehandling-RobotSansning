import cv2
import numpy as np

img = cv2.imread('mini projekt/1.jpg')
average_color_row = np.average(img, axis=0)
average_color = np.average(average_color_row, axis=0)
print(average_color)

cv2.waitKey(0)