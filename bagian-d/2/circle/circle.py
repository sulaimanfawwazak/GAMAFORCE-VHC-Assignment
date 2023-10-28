import cv2 as cv
import numpy as np

# Source image
source = cv.imread('circle/circle.png')

# Copy the image to be processed
processed = source.copy()

# Convert BGR into HSV
hsv = cv.cvtColor(processed, cv.COLOR_BGR2HSV)

# Threshold value
lower_yellow = np.array([20, 50, 200], dtype=np.uint8)
upper_yellow = np.array([100, 200, 255], dtype=np.uint8)

# Masking
mask = cv.inRange(hsv, lower_yellow, upper_yellow)

result = cv.bitwise_and(processed, processed, mask=mask)

cv.imshow('result', result)
cv.waitKey(0)

# Blur the image
result = cv.GaussianBlur(result, (9, 9), 11)

kernel = np.ones((20, 20), np.uint8)
result = cv.morphologyEx(result, cv.MORPH_CLOSE, kernel)
result = cv.cvtColor(result, cv.COLOR_BGR2GRAY)

cv.imshow('Holes filled', result)
cv.waitKey(0)
cv.destroyAllWindows()

# Begin Hough Transform
circles = cv.HoughCircles(result, cv.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=130, maxRadius=0)

if circles is not None:
  circles = np.uint16(np.around(circles))
  for circle in circles[0, :]:
    center = (circle[0], circle[1])
    radius = circle[2]

    # Font
    font = cv.FONT_HERSHEY_SIMPLEX
    text = '+'
    text_size = cv.getTextSize(text, font, 1, 2)[0]
    
    text_x = center[0] - text_size[0] // 2
    text_y = center[1] - text_size[1] // 2 
    
    cv.putText(source, text, (text_x, text_y), font, 1, (255, 0, 255), 2, cv.LINE_AA)

    cv.circle(source, center, radius, (0, 255, 0), 2)

  cv.imshow('Img', source)
  cv.waitKey(0)
  cv.destroyAllWindows()
else:
  print("No circles found in the image.")
