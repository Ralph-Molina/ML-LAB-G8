import cv2

path = r'C:\\Users\\STUDENT\\Desktop\\Sample image\\OIF.jpg'

img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

cv2.imshow('OIF.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()