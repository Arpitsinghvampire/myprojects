from statistics import mode
from traceback import TracebackException
import cv2 as cv
import mediapipe as mp
import time 
cap=cv.VideoCapture(0)
mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils
p_time=0
c_time=0  
while True:
    success,img=cap.read()
    color=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    results=hands.process(color)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                print(id,cx,cy)
                if(id==4):
                    cv.circle(img,(cx,cy),25,(255,0,255),cv.FILLED)
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
    c_time=time.time()
    fps=1/c_time-p_time
    p_time=c_time
    cv.putText(img,str(fps),(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
    cv.imshow('image',img)
    cv.waitKey(1)
def main():
    ptime=0
    ctime=0
    mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils
p_time=0
c_time=0  
while True:
    success,img=cap.read()
    color=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    results=hands.process(color)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                print(id,cx,cy)
                if(id==4):
                    cv.circle(img,(cx,cy),25,(255,0,255),cv.FILLED)
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
    c_time=time.time()
    fps=1/c_time-p_time
    p_time=c_time
    cv.putText(img,str(fps),(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
    cv.imshow('image',img)
    cv.waitKey(1)
def handDetector():
    def __init__(self,mode=False,maxHands=2,minconfidence=0.5,min1confidence=0.5):
        self.mode=mode
        self.maxHands=maxHands
        self.detectionCon=minconfidence
        self.trackCon=min1confidence
        


    
