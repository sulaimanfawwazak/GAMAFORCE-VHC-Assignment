import cv2 as cv
import numpy as np
import math

# width and height of the image
width, height = 255, 255

# mid pixel
mid_x, mid_y = 128, 128

# make the image, with each pixel's value = 0
image = np.zeros((height, width), dtype=np.uint8)

cv.imwrite('initial-gray.png', image)

# iterates through the rows (height)
for y in range (height):
  #iterates through the columns (width)
  for x in range (width):

    # calculate the euclidean distance from each pixel to the center
    distance = math.sqrt(pow(x - mid_x, 2) + pow(y - mid_y, 2))

    # set the pixel's value as the distance
    image[x][y] = distance

cv.imwrite("./grayscale/gray-image.png", image)

cv.imshow("Gray Image", image)
cv.waitKey(0)
cv.destroyAllWindows()