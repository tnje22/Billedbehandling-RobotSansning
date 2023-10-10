import cv2
import numpy as np

img = cv2.imread('mini projekt/1.jpg')
cv2.imshow("original", img)

squares = []
average_colors = []

# Define the size of each square
square_size = 100

# Iterate over rows and columns to crop and calculate average color
for y in range(5):
    for x in range(5):
        square = img[y * square_size:(y + 1) * square_size, x * square_size:(x + 1) * square_size]
        squares.append(square)
        average_color = np.average(square, axis=(0, 1))
        average_colors.append(average_color)

# Display the cropped squares and their average colors
for i, (square, average_color) in enumerate(zip(squares, average_colors), 1):
    #cv2.imshow(f"Square {i}", square)
    print(f"Average Color for Square {i}: {average_color}")
#average_colors er en liste og de starter fra 0 så nummer 4 i listen er square 5
#print(average_colors[4])
cv2.waitKey(0)
cv2.destroyAllWindows()