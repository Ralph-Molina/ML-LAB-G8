import cv2 as cv
from matplotlib import pyplot as plt

# Read the image
img = cv.imread('drake.jpg')

# Apply blur
blur = cv.blur(img, (7, 7))

# Display the original and blurred images
plt.subplot(121), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)), plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(cv.cvtColor(blur, cv.COLOR_BGR2RGB)), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()