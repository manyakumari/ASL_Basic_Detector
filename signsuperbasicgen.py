import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
from gtts import gTTS
import os

language = 'en'
cap = cv.VideoCapture(0)
detector = HandDetector(maxHands=2,detectionCon=0.8)
while True:
    ret,frame = cap.read()
    hands,img = detector.findHands(frame)
    if hands:
        left = hands[0]
        lmList = left['lmList']
        bbox =left['bbox']
        center = left['center']
        htype = left['type']
        fingers = detector.fingersUp(left)
        if fingers == [0,0,0,0,1]:
            text1 = "I"
            print(text1)
            ''' myobj = gTTS(text=text1, lang=language, slow=False)
            myobj.save("aslpractice.mp3")
            os.system("mpg321 aslpractice.mp3")'''
        if fingers == [0,1,1,0,0]:
            text1 = "YOU"
            print(text1)
        if fingers == [0,1,1,1,0]:
            text1 = "W"
            print(text1)
        if fingers == [0,1,1,1,1]:
            text1 = "B"
            print(text1)
        if fingers == [1,0,0,0,1]:
            text1 = "Y"
            print(text1)
        if fingers == [1,1,0,0,1]:
            text1 = "I LOVE YOU"
            print(text1)
        if fingers == [1,0,0,0,0]:
            text1 = "thumbs up"
            print(text1)
        if fingers == [1,1,0,0,0]:
            text1 = "L"
            print(text1)
    cv.imshow("finals",img)
    key = cv.waitKey(5)
    if key == 27:
        break