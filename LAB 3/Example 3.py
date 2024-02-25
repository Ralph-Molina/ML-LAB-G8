import cv2 as cv
from matplotlib import pyplot as plt

# Read the image
img = cv.imread('drake.jpg')

# Apply median blur
median = cv.medianBlur(img, 19)

# Display the original and blurred images
plt.subplot(121), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)), plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(cv.cvtColor(median, cv.COLOR_BGR2RGB)), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()