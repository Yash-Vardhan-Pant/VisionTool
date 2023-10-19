#import numpy as np
#import pyautogui
#import imutils
import threading
import pyttsx3
import cv2
import time
# new


def thread_voice_alert(engine):
    engine.say("Motion")
    engine.runAndWait()


# new
status_list = [None, None]
video = cv2.VideoCapture(0)
#result, image=video.read()

# voice engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
first_frame = None

while True:
    check, frame = video.read()
    # new
    status = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    if first_frame is None:
        first_frame = gray
        continue
    delta_frame = cv2.absdiff(first_frame, gray)
    threshold_frame = cv2.threshold(delta_frame, 50, 255, cv2.THRESH_BINARY)[1]
    threshold_frame = cv2.dilate(threshold_frame, None, iterations=2)

    (cntr, _) = cv2.findContours(threshold_frame.copy(),
                                 cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cntr:
        if cv2.contourArea(contour) < 1000:
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
    status_list.append(status)

    if status_list[-1] == 1 and status_list[-2] == 0:
        t = threading.Thread(target=thread_voice_alert, args=(engine,))
        t.start()

    cv2.imshow("cvghj", frame)


    key = cv2.waitKey(1)
    if key == ord('q'):
        break
engine.stop()
video.release()
cv2.destroyAllWindows()
