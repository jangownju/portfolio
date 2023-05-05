import socket
import threading
import time
import cv2

local_ip = ''
local_port = 8889 # port for receiving Tello Response
local_addr = (local_ip, local_port)
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(local_addr)

tello_ip = '192.168.10.1'
tello_port = 8889
tello_addr = (tello_ip, tello_port)

response = None
def _receive_thread():
    global response
    while True:
        try:
            response, ip = socket.recvfrom(1024)
            print(f'from {ip}: {response}')
        except Exception as e:
            print(f'Caught exception {e}')
# thread for receiving cmd ack
receive_thread = threading.Thread(target=_receive_thread)
receive_thread.daemon=True
receive_thread.start()

def send_command(command):
    global response
    start = time.time()
    socket.sendto(command.encode('utf-8'), tello_addr)
    print(f'Sending Command: {command} to {tello_addr}')
    while not response: time.sleep(0.01)
    response = None
    end = time.time()
    diff=end-start
    print(f'Done!!! sent command: {command} to {tello_addr} for {diff:.3f} sec')
def _send_command_without_return(command):
    socket.sendto(command.encode('utf-8'), tello_addr)
    print(f'Sending Command: {command} to {tello_addr}(no response expected)')
def send_rc_control(lrv,fbv,udv,yawv):
    command=f'rc {lrv} {fbv} {udv} {yawv}'
    _send_command_without_return(command)

send_command('command')
send_command('battery?')
send_command('streamon')

# streamon 명령 전에 오면 다음 루틴은 blocking

capture = cv2.VideoCapture('udp://0.0.0.0:11111', cv2.CAP_FFMPEG)
while True:
    try:
        ret, frame = capture.read()
        if frame is None or frame.size == 0:
            continue

#frame = cv2.resize(frame,(360,240))
        cv2.imshow('frame', frame)
        if cv2.waitKey(1)&0xFF == ord ('q'):
            break
    except Exception as e:
        print(f'Caught exception {e}')