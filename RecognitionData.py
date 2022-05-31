import cv2
import sqlite3
import numpy as np
from PIL import Image


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("recognizer/trainningData.yml")


# get data from sqlite by ID
def getProfile(id):
    conn = sqlite3.connect("data.db")
    query = "SELECT * FROM Student WHERE ID="+str(id)  # nhớ gi đừng quên
    cursor = conn.execute(query)

    profile = None
    for row in cursor:
        profile = row
    conn.close()
    return profile


cap = cv2.VideoCapture(0)
fontface = cv2.FONT_HERSHEY_SIMPLEX
while(True):
    # camera read
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 225, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        id, conf = recognizer.predict(roi_gray)
        profile = getProfile(id)
        # set text to window
        # if(conf < 40):
        profile = getProfile(id)
        if(profile != None):
            # mình sẽ in tên mình ra tên ở vtri thứ 1,fontface màu chữ còn 2 độ dày chữ x,y vị trí
            cv2.putText(
                frame, "Name :" + str(profile[1]), (x+10, y+h + 30), fontface, 1, (0, 255, 0), 2)
            cv2.putText(
                frame, "Age :" + str(profile[2]), (x+10, y+h + 60), fontface, 1, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "Unknow", (x+10, y+h+30),
                        fontface, 1, (0, 0, 255), 2)
        cv2.imshow('Face', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
