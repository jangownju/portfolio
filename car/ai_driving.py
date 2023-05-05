import socket
import time
import struct

import cv2
import numpy as np

from tensorflow.keras.models import load_model
import tensorflow as tf

cap = cv2.VideoCapture('http://192.168.4.1:81/stream')

CAM_IP = '192.168.4.1'
MOT_PORT = 82
MOT_ADDR = (CAM_IP, MOT_PORT)

mot_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

t_now = time.time()
t_prev = time.time()
cnt_frame = 0

model = load_model('model.h5')

names = ['_0_forward', '_1_right', '_2_left', '_3_stop']

while True:
	# 영상 받기
	ret, frame = cap.read()

	# 영상 출력
	frame = cv2.rotate(frame,cv2.ROTATE_180)
	cv2.imshow('frame', frame)

	frame = cv2.resize(frame, (160, 120))

	image = frame
	image = image/255

	image_tensor = tf.convert_to_tensor(image, dtype=tf.float32)
	# print(image_tensor.shape)

	# Add dimension to match with input mode
	image_tensor = tf.expand_dims(image_tensor, 0)
	# print(image_tensor.shape)

	y_predict = model.predict(image_tensor)
	y_predict = np.argmax(y_predict,axis=1)
	print(names[y_predict[0]], y_predict[0])

	# send y_predict
	cmd = y_predict[0].item()
	cmd = struct.pack('B', cmd)
	mot_socket.sendto(cmd, MOT_ADDR)

	key = cv2.waitKey(1)
	if key == 27:
		break

	cnt_frame += 1
	t_now = time.time()
	if t_now - t_prev >= 1.0 :
		t_prev = t_now
		print("frame count : %f" %cnt_frame)
		cnt_frame = 0

mot_socket.close()