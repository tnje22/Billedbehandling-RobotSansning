import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('mini projekt/1.jpg')
cv2.imshow("original", img)

squares = []

# Define the size of each square
square_size = 100

# Iterate over rows and columns to crop squares
for y in range(5):
    for x in range(5):
        square = img[y * square_size:(y + 1) * square_size, x * square_size:(x + 1) * square_size]
        squares.append(square)

# Display the cropped squares and their histograms
for i, square in enumerate(squares, 1):
    cv2.imshow(f"Square {i}", square)
    
    # Calculate the histogram
    hist = cv2.calcHist([square], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
    
    # Plot the histogram
    plt.figure()
    plt.title(f"Histogram for Square {i}")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.plot(hist[:, 0], color='b', label='Blue Channel')
    plt.plot(hist[:, 1], color='g', label='Green Channel')
    plt.plot(hist[:, 2], color='r', label='Red Channel')
    plt.xlim([0, 256])
    plt.legend(loc='upper right')
    plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
