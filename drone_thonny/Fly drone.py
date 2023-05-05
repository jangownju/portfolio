import socket
import threading
import time

local_ip = ''
local_port = 8889 # port for receiving Tello Response
local_addr = (local_ip, local_port)
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(local_addr)

tello_ip = '192.168.10.1'
tello_port = 8889
tello_addr = (tello_ip, tello_port)

socket.sendto('command'.encode('utf-8'), tello_addr) # must!
print(f'Sending Command: command to {tello_addr}')
time.sleep(0.1) # 0.1초

def _receive_thread():
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

socket.sendto('takeoff'.encode('utf-8'), tello_addr)
print(f'Sending Command: takeoff to {tello_addr}')
time.sleep(10.0) # 8.7초

socket.sendto('land'.encode('utf-8'), tello_addr)
print(f'Sending Command: land to {tello_addr}')
time.sleep(5.0) # 3.8초