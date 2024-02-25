import cv2 as cv
from matplotlib import pyplot as plt

vid = cv.VideoCapture(0)

while True:
    ret, frame = vid.read()
    if not ret:
        break

    frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    blur_frame = cv.blur(frame_rgb, (5, 5), 0)

    sobelx = cv.Sobel(blur_frame, cv.CV_64F, 1, 0, ksize=5)
    filtered_frame_x = cv.convertScaleAbs(sobelx)

    sobely = cv.Sobel(blur_frame, cv.CV_64F, 0, 1, ksize=5)
    filtered_frame_y = cv.convertScaleAbs(sobely)

    sobelxy = cv.Sobel(blur_frame, cv.CV_64F, 1, 1, ksize=5)
    filtered_frame_xy = cv.convertScaleAbs(sobelxy)

    plt.figure(figsize=(10, 5))

    plt.subplot(2, 2, 1)
    plt.imshow(frame_rgb)
    plt.title('Original')

    plt.subplot(2, 2, 2)
    plt.imshow(filtered_frame_x, cmap='gray')
    plt.title('Sobel X')

    plt.subplot(2, 2, 3)
    plt.imshow(filtered_frame_y, cmap='gray')
    plt.title('Sobel Y')

    plt.subplot(2, 2, 4)
    plt.imshow(filtered_frame_xy, cmap='gray')
    plt.title('Sobel XY')

    plt.tight_layout()
    plt.show()

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv.destroyAllWindows()