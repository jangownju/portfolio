from mytello import Tello
import KeyPressedModule as kp
import time

kp.init()
tello = Tello()

tello.command()
tello.battery()

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
    
    return [lr,fb,ud,yv]
while True:
    lr,fb,ud,yv=getKeyboardInput()
    tello.send_rc_control(lr,fb,ud,yv)
    time.sleep(0.05)
