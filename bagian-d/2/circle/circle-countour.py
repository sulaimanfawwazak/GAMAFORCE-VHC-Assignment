import cv2 as cv
import numpy as np

# Load the image
source = cv.imread('circle/circle.png')

# Make a copy of the image to be processed
processed = source.copy()

# Do the color detection
## Convert into hsv
hsv = cv.cvtColor(processed, cv.COLOR_BGR2HSV)

## Create the threshold
lower_yellow = np.array([20, 50, 200], dtype=np.uint8)
upper_yellow = np.array([100, 200, 255], dtype=np.uint8)

## Make the mask
mask = cv.inRange(hsv, lower_yellow, upper_yellow)

mask = cv.medianBlur(mask, 51)

cv.imshow('Mask', mask)
cv.waitKey(0)

## Convert into binary image
ret, thresh = cv.threshold(mask, 127, 255, 0)

cv.imshow('thresh', thresh)
cv.waitKey(0)

kernel = np.ones((5, 5), np.uint8)
thresh = cv.morphologyEx(thresh, cv.MORPH_ERODE, kernel)

# Find the contours
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

## Draw the contours
for contour in contours:
  if cv.contourArea(contour) > 400:

    (x, y), radius = cv.minEnclosingCircle(contour)
    center = (int(x), int(y))

    cv.circle(source, center, int(radius), (0, 255, 0), 2)
    cv.circle(source, center, 2, (0, 255, 0), 2)

    ### Line
    cv.line(source, (center[0], center[1] + 50), (center[0], center[1] - 50), (255, 0, 255), 5)
    cv.line(source, (center[0] + 50, center[1]), (center[0] - 50, center[1]), (255, 0, 255), 5)


source = cv.resize(source, (0, 0), fx=0.5, fy=0.5)

cv.imshow('Image', source)
cv.imwrite('circle-plus-sign.png', source)
cv.waitKey(0)
cv.destroyAllWindows()