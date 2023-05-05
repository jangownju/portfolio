from PyQt5.QtWidgets import *
import sys
import threading

from myjoystick import MyJoystick

from PyQt5 import QtWidgets
import cv2
import time
from PyQt5 import QtGui

cap = cv2.VideoCapture("http://192.168.4.1:81/stream")

t_now = time.time()
t_prev = time.time()
cnt_frame = 0
total_frame = 0
cnt_time = 0

def camMain() :
    global t_now, t_prev, cnt_frame, total_frame, cnt_time
    
    width = 320
    height = 240
    label.resize(width, height)
    
    while True:
# 영상 받기
            ret, frame = cap.read()

# 영상 출력
# frame = cv2.rotate(frame,cv2.ROTATE_180)
            frame2 = cv2.resize(frame, (320, 240))
            
            h,w,c = frame2.shape
            qImg = QtGui.QImage(frame2.data, w, h, w*c, \
            QtGui.QImage.Format_RGB888)
            pixmap = QtGui.QPixmap.fromImage(qImg.rgbSwapped())
            label.setPixmap(pixmap)
            
            cnt_frame += 1
            t_now = time.time()
            if t_now - t_prev >= 1.0 :
                    t_prev = t_now
                    total_frame += cnt_frame
                    cnt_time += 1
                    print("frame count : %f, %d average : %f" \
                    %(cnt_frame, cnt_time, total_frame/cnt_time))
                    cnt_frame=0

def cbJoyPos(joystickPosition) :
    posX, posY = joystickPosition
    # 자동차 방향
    right, left = -1, -1
    if posY < -0.5:
        right, left = 1, 1
        print('brake')
    elif posY > 0.15 :
        if -0.15 <= posX <= 0.15 :
            right, left = 0, 0
            print('forward')
            elif posX < -0.15 :
                right, left = 1, 0
                print('left')
            elif posX > 0.15 :
                right, left = 0, 1
                print('right')
    else : # -0.5 <= posY <= 0.15
        print('stop driving')

# Create main application window
app = QApplication([])
app.setStyle(QStyleFactory.create("Cleanlooks"))
mw = QMainWindow()
mw.setWindowTitle('RC Car Joystick')
mw.setGeometry(100, 100, 300, 200)

# Create and set widget layout
# Main widget container
cw = QWidget()
ml = QGridLayout()
cw.setLayout(ml)
mw.setCentralWidget(cw)

# Create Screen
label = QtWidgets.QLabel()
ml.addWidget(label,0,0)

# Create joystick
joystick = MyJoystick(cbJoyPos)
ml.addWidget(joystick,1,0)

camThread = threading.Thread(target=camMain)
camThread.daemon = True
camThread.start()

mw.show()

# Start Qt event loop
sys.exit(app.exec_())