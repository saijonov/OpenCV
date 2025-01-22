import cv2  as cv

# #reading images
# image = cv.imread("data/photos/cat_bigger.jpeg")
# cv.imshow("Cat", image)
# cv.waitKey(0)

#reading videos
capture = cv.VideoCapture("data/videos/IMG_2828.MOV")
while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

