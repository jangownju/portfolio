import cv2
import time

cap = cv2.VideoCapture("http://192.168.4.1:81/stream")

t_now = time.time()
t_prev = time.time()
cnt_frame = 0
total_frame = 0
cnt_time = 0

while(True):
	# 영상 받기
	ret, frame = cap.read()

	# 영상 출력
	# frame = cv2.rotate(frame,cv2.ROTATE_180)
	frame2 = cv2.resize(frame, (320, 240))
	cv2.imshow('frame',frame2)

	key = cv2.waitKey(1)
	if key == 27:
		break

	cnt_frame += 1
	t_now = time.time()
	if t_now - t_prev >= 1.0 :
		t_prev = t_now
		total_frame += cnt_frame
		cnt_time += 1
		print("frame count : %f, %d average : %f" \
		%(cnt_frame, cnt_time, total_frame/cnt_time))
		cnt_frame = 0

cap.release()
cv2.destroyAllWindows()