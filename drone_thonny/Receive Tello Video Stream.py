import socket

local_ip = ''
local_port = 11111 # port for receiving Tello Video Stream
local_addr = (local_ip, local_port)
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(local_addr)

tello_ip = '192.168.10.1'
tello_port = 8889
tello_addr = (tello_ip, tello_port)

socket.sendto('command'.encode('utf-8'), tello_addr) # tello.connect, must!
socket.sendto('streamon'.encode('utf-8'), tello_addr)

while True:
    try:
        response, ip = socket.recvfrom(2048)
        print(f'from {ip}: {response}')
    except Exception as e:
        print(f'Caught exception {e}')
        break