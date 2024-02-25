import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('drake.jpg')
blur = cv.bilateralFilter(img, 9,75,75)


plt.subplot(121), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)), plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(cv.cvtColor(blur, cv.COLOR_BGR2RGB)), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()