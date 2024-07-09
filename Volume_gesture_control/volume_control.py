import cv2 as cv
import mediapipe as mp
import numpy as np
import time
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


video = cv.VideoCapture(0)

mphands = mp.solutions.hands #type:ignore
hands = mphands.Hands(min_detection_confidence = 0.8)
mpdraw = mp.solutions.drawing_utils #type:ignore
ptime = 0

def volume_gesture_control(lmlist):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)

    vol_range = volume.GetVolumeRange()
    min_vol = vol_range[0]
    max_vol = vol_range[1]

    bar = 300

    x1,y1 = lmlist[4][1], lmlist[4][2]
    x2,y2 = lmlist[8][1], lmlist[8][2]

    cx,cy = (x1+x2)//2,(y1+y2)//2

    cv.circle(frame,(x1,y1),10,(0,255,0),-1)
    cv.circle(frame,(x2,y2),10,(0,255,0),-1)
    cv.line(frame,(x1,y1),(x2,y2),(0,0,255),2)
    cv.circle(frame,(cx,cy),10,(255,0,0),-1)

    length = math.hypot(x2-x1,y2-y1)

    vol = np.interp(length,[20,160],[min_vol,max_vol])
    bar = np.interp(length,[20,160],[300,80])

    volume.SetMasterVolumeLevel(vol, None)

    cv.rectangle(frame,(40,80),(60,300),(255,0,0),2)
    cv.rectangle(frame,(40,int(bar)),(60,300),(255,0,0),-1)



while True:
    isTrue, frame = video.read()
    rgbframe = cv.cvtColor(frame,cv.COLOR_BGR2RGB)

    result = hands.process(rgbframe)
    lmlist = []
    if result.multi_hand_landmarks:
        for handlms in result.multi_hand_landmarks:
            for i,lms in enumerate(handlms.landmark):
                h,w,c = frame.shape
                x,y = int(lms.x*w), int(lms.y*h)
                lmlist.append([i,x,y])
 
            mpdraw.draw_landmarks(frame,handlms, mphands.HAND_CONNECTIONS)

    if len(lmlist)!=0:
        volume_gesture_control(lmlist)
        
    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv.putText(frame, str(int(fps)), (20,30), cv.FONT_HERSHEY_PLAIN,3,(0,255,0),4)
    cv.imshow('Frame', frame)

    if cv.waitKey(1) & 0xff==ord('q'):
        break
video.release()