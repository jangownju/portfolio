import pygame

def init():
    pygame.init()
    win=pygame.display.set_mode((400,400)) # 크기는 상관없다.
    
def getKey(keyName):
    ans = False
    for eve in pygame.event.get():
 #print(eve)
        pass
    keyInput=pygame.key.get_pressed()
 #print(keyInput, type(keyInput))
    
    myKey=getattr(pygame, f'K_{keyName}')
    if keyInput[myKey]:
        ans=True
    pygame.display.update()
    
    return ans

def main():
 #print(getKey('a'))
 #getKey('a')
    if getKey('LEFT'):
        print('Left key pressed')
    if getKey('RIGHT'):
        print('RIGHT key pressed')

if __name__ == '__main__':
    init()
    while True:
        main()