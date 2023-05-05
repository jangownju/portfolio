from mytello import Tello
import KeyPressedModule as kp
import time
import cv2

kp.init()
tello = Tello()

tello.command()
tello.battery()

tello.streamon()

def getKeyboardInput():
    lr, fb, ud, yv = 0,0,0,0
    speed=50
    if kp.getKey('LEFT'): lr = -speed
    elif kp.getKey('RIGHT'): lr = speed
    
    if kp.getKey('UP'): fb = speed
    elif kp.getKey('DOWN'): fb = -speed
    
    if kp.getKey('w'): ud = speed
    elif kp.getKey('s'): ud = -speed
    
    if kp.getKey('a'): yv = speed
    elif kp.getKey('d'): yv = -speed
    
    if kp.getKey('q'): tello.land()
    if kp.getKey('e'): tello.takeoff()
    
    if kp.getKey('z'): # 사진 찍기, 디렉터리 생성해 줄것!
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg',img)
        time.sleep(0.3) # 없으면 사진이 너무 많이 생성
        
    return [lr,fb,ud,yv]

while True:
    lr,fb,ud,yv=getKeyboardInput()
    tello.send_rc_control(lr,fb,ud,yv)
    img = tello.get_frame()
    if img is None or img.size == 0:
        continue
    img = cv2.resize(img,(360,240))
    cv2.imshow('Image', img)
    cv2.waitKey(1)
