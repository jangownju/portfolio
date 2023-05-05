import socket
import cv2

local_ip = ''
local_port = 8889 # port for receiving Tello Response
local_addr = (local_ip, local_port)
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(local_addr)

tello_ip = '192.168.10.1'
tello_port = 8889
tello_addr = (tello_ip, tello_port)

socket.sendto('command'.encode('utf-8'), tello_addr) # tello.connect, must!
socket.sendto('streamon'.encode('utf-8'), tello_addr)

capture = cv2.VideoCapture ('udp://0.0.0.0:11111', cv2.CAP_FFMPEG)

while True:
    try:
        ret, frame = capture.read()
        if ret:
            cv2.imshow('frame', frame)
            
        if cv2.waitKey(1)&0xFF == ord ('q'):
            break
