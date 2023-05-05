from mytello import Tello
import cv2
import numpy as np

faceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

tello=Tello()
tello.command()
tello.battery()

tello.streamon()
# tello.takeoff()
tello.up(80)
cx,cy=0,0
area=0
while True:
    frame=tello.get_frame()
    if frame is None or frame.size==0:
        continue
    image=cv2.resize(frame,(320,240))
    imageGray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(imageGray, 1.1, 8)
    cx,cy=0,0
    area=0#
    for x,y,w,h in faces:
        cv2.rectangle(image, (x,y),(x+w,y+h),(0,0,255), 2)
        cx=x+w//2
        cy=y+h//2
        area=w*h
        cv2.circle(image,(cx,cy),5,(0,255,0),cv2.FILLED)
        print(area)
    h,w,d=image.shape
    cv2.circle(image,(w//2,h//2),5,(0,0,255),cv2.FILLED)
    xE=cx-w//2
    yE=cy-h//2
    aE=area-10000#
    print(xE, yE, aE)
    # 1. up down으로 얼굴 쫓아 다니기
    if not (cx==0 and cy==0):
        udv=-yE//2
        udv=int(np.clip(udv,-50,50))
    # 2. yaw로 얼굴 쫓아 다니기
        yav=xE//2
        yav=int(np.clip(yav,-50,50))
#         tello.send_rc_control(0,0,udv,yav)
    # 3. 일정 거리 유지하기
        fbv=-aE//2
        fbv=int(np.clip(fbv,-10,10))
        tello.send_rc_control(0,fbv,udv,yav)
    else: tello.send_rc_control(0,0,0,0)

    cv2.imshow('Frame',image)
    if cv2.waitKey(1)&0xFF==ord('q'):
        tello.land()
        break
cv2.destroyAllWindows()

tello._send_command_without_return('reboot')