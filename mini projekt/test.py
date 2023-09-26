import cv2
import numpy as np

img = cv2.imread('mini projekt/1.jpg')

# Define the size of each square
square_size = 100

# Initialize a list to store histograms
histograms = []

# Iterate over rows and columns to crop and calculate histograms
for y in range(5):
    for x in range(5):
        square = img[y * square_size:(y + 1) * square_size, x * square_size:(x + 1) * square_size]
        hist = cv2.calcHist([square], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
        histograms.append(hist)

# Perform histogram comparison pairwise
for i in range(len(histograms)):
    for j in range(i + 1, len(histograms)):
        intersection = cv2.compareHist(histograms[i], histograms[j], cv2.HISTCMP_INTERSECT)
        print(f'Histogram Intersection between Square {i + 1} and Square {j + 1}: {intersection}')