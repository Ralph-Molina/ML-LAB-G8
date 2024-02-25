import cv2 as cv
from matplotlib import pyplot as plt

vid = cv.VideoCapture(0)

while True:
    ret, frame = vid.read()
    if not ret:
        break

    frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    laplacian = cv.Laplacian(frame_gray, cv.CV_64F)
    filtered_image = cv.convertScaleAbs(laplacian)

    plt.figure(figsize=(10, 5))

    plt.subplot(2, 2, 1)
    plt.imshow(frame_rgb)
    plt.title('Original')

    plt.subplot(2, 2, 2)
    plt.imshow(filtered_image, cmap='gray')
    plt.title('Laplacian')

    plt.tight_layout()
    plt.show()

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv.destroyAllWindows()