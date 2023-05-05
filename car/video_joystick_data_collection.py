import sys
import threading

from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5 import QtGui
				
from myjoystick import MyJoystick

import socket
import time
import struct
import cv2

import os
import csv

cap = cv2.VideoCapture('http://192.168.4.1:81/stream')

CAM_IP = '192.168.4.1'
MOT_PORT = 82
MOT_ADDR = (CAM_IP, MOT_PORT)

mot_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

t_now = time.time()
t_prev = time.time()
cnt_frame = 0

cnt_frame_total = 0

dirname = "data.%f" %(time.time())
os.mkdir(dirname)
os.mkdir(os.path.join(dirname, "_0_forward"))
os.mkdir(os.path.join(dirname, "_1_right"))
os.mkdir(os.path.join(dirname, "_2_left"))
os.mkdir(os.path.join(dirname, "_3_stop"))

f_csv = open(os.path.join(dirname, "0_road_labels.csv"),'w', newline='')
wr = csv.writer(f_csv)
wr.writerow(["file","label"])

names = ['_0_forward', '_1_right', '_2_left', '_3_stop']

g_rl = 0

def camMain() :
	global t_now, t_prev, cnt_frame, cnt_frame_total

	width = 320
	height = 240
	label.resize(width, height)

	while True:
		# 영상 받기
		ret, frame = cap.read()

		# 영상 출력
		frame = cv2.rotate(frame,cv2.ROTATE_180)
		
		frame2 = cv2.resize(frame, (320, 240))
		frame = cv2.resize(frame, (160, 120))
		 
		h,w,c = frame2.shape
		qImg = QtGui.QImage(frame2.data, w, h, w*c, \
			QtGui.QImage.Format_RGB888)
		pixmap = QtGui.QPixmap.fromImage(qImg.rgbSwapped())
		label.setPixmap(pixmap)
		
		rl = g_rl
		collect_data = (rl & 4)>>2
		rl = rl & 3

		if (collect_data==1) :
			road_file = "%f.png" %(time.time())
			cv2.imwrite(
				os.path.join(os.path.join(dirname, names[rl]),\
				road_file),
				frame)
			wr.writerow([os.path.join(names[rl], road_file),rl])
			f_csv.flush()			
			cnt_frame_total += 1

		cnt_frame += 1
		t_now = time.time()
		if t_now - t_prev >= 1.0 :
			t_prev = t_now
			print("frame count : %d" %cnt_frame, \
				"total frame : %d" %cnt_frame_total)
			cnt_frame = 0
			
def cbJoyPos(joystickPosition) :
	global g_rl
	posX, posY = joystickPosition
		
	# 자동차 방향
	right, left = -1, -1
	collect_data = 1
	if posY < -0.5:
		right, left = 1, 1 # brake
	elif posY > 0.15 :
		if -0.15 <= posX <= 0.15 :
			right, left = 0, 0 # forward
		elif posX < -0.15 : 
			right, left = 1, 0 # left
		elif posX > 0.15 :
			right, left = 0, 1 # right
	else : # -0.5 <= posY <= 0.15
		right, left = 1, 1 # stop driving
		collect_data = 0

	rl = collect_data << 2 | right << 1 | left
	g_rl = rl
	rl_byte = struct.pack('B', rl)
	mot_socket.sendto(rl_byte, MOT_ADDR)

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