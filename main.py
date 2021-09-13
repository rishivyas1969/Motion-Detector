import cv2, time, numpy

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    check, frame = video.read()
    # print(check)
    # print(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("ME", numpy.flip(gray, 1))
    key = cv2.waitKey(1)

    if key == ord('m'):
        break

cv2.destroyAllWindows()

video.release()