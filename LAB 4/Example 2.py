import cv2 as cv
from matplotlib import pyplot as plt

vid = cv.VideoCapture(0)

while True:
    ret, frame = vid.read()
    if not ret:
        break

    frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    blur_frame = cv.blur(frame_rgb, (5, 5), 0)

    edges = cv.Canny(blur_frame, 100, 200)

    plt.figure(figsize=(10, 5))

    plt.subplot(2, 2, 1)
    plt.imshow(frame_rgb)
    plt.title('Original')

    plt.subplot(2, 2, 2)
    plt.imshow(edges, cmap='gray')
    plt.title('Canny')

    plt.tight_layout()
    plt.show()

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv.destroyAllWindows()