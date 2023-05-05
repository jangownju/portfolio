import socket

local_ip = ''
local_port = 8890 # port for receiving Tello State
local_addr = (local_ip, local_port)
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(local_addr)

tello_ip = '192.168.10.1'
tello_port = 8889
tello_addr = (tello_ip, tello_port)

socket.sendto('command'.encode('utf-8'), tello_addr) # tello.connect, must!

while True:
    try:
        response, ip = socket.recvfrom(1024)
        print(f'from {ip}: {response}')
    except Exception as e:
        print(f'Caught exception {e}')
        break
