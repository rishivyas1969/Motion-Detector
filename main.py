import cv2, time, numpy
from datetime import datetime
import pandas

df = pandas.DataFrame(columns=['Entry', 'Exit'])

first_frame = None
video = cv2.VideoCapture(0)

status_list = [None, None]
times = []

while True:
    check, frame = video.read()

    status = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    (cnts, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contours in cnts:
        if cv2.contourArea(contours) < 1000 :
            continue

        status = 1
        (x, y, w, h) = cv2.boundingRect(contours)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 3)

    status_list.append(status)
    if status_list[-1] == 0 and status_list[-2] == 1:
        entry_time = datetime.now()
    
    if status_list[-1] == 0 and status_list[-2] == 1:
        exit_time = datetime.now()
        times.append([entry_time, exit_time])


    cv2.imshow('Color Frame', frame)
    cv2.imshow('Delta Frame', delta_frame)
    cv2.imshow('Threshold Frame', thresh_frame)

    cv2.imshow("ME", numpy.flip(gray, 1))
    key = cv2.waitKey(1)

    if key == ord('m'):
        if status == 1:
            times.append([entry_time, datetime.now()])
        break

for i in times:
    df = df.append({'Entry': i[0], 'Exit': i[1]}, ignore_index=True)

df.to_csv('Times.csv')

cv2.destroyAllWindows()

video.release()