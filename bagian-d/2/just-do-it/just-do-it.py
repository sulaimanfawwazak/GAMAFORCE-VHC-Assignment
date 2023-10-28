import cv2 as cv
import numpy as np

# Load the image
img = cv.imread('just-do-it/just-do-it.png', 1)

# Convert into HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# Set the threshold value
lower_red = np.array([0, 115, 0], dtype=np.uint8)
upper_red = np.array([15, 255, 255], dtype=np.uint8)

# Make the mask
mask = cv.inRange(hsv, lower_red, upper_red)

# result = cv.bitwise_and(img, img, mask=mask)

cv.imshow("Image", img)
cv.imshow("Mask", mask)
cv.imwrite("just-do-it-output.png", mask)
# cv.imshow("Result", result)
cv.waitKey(0)
cv.destroyAllWindows()