import cv2
import numpy as np

input = cv2.imread("lion.jpg")
output = np.zeros(input.shape, dtype=input.dtype)

for y, row in enumerate(input):
    for x, pixel in enumerate(row):
        value = np.max(pixel)
        saturation = 0
        if value != 0:
            saturation = (value - np.min(pixel))/value
        hue = 0
        h_denominator = value - np.min(pixel)

        blue, green, red = int(blue), int(green), int(red)
        bgr = [int(a) for a in pixel]
        blue, green, red = bgr

        if h_denominator != 0:
            if value == red and green >= blue:
                hue = (green-blue)/h_denominator*60
            elif value == green:
                hue = ((blue-red)/h_denominator + 2)*60
            elif value == blue:
                hue = ((red - green) / h_denominator + 4) * 60
            elif value == red and green < blue:
                hue = ((red - blue) / h_denominator + 5) * 60
        hue /= 2
        output[y, x] = [hue, saturation, value]



cv2.imshow("Input", input)
cv2.imshow("Output", output)
cv2.imshow("Hue", output[:,:,0])
cv2.waitKey(0)