import cv2
import matplotlib.pyplot as plt


img = cv2.imread("C:\\Users\\STUDENT\\Desktop\\Sample image\\OIF.jpg")
plt.imshow(img)


plt.waitforbuttonpress()
plt.close('all')
