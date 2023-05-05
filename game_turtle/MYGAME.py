import turtle

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("MYGAME.gif")

#게임 단계
border_pen=turtle.Turtle()
border_pen.hideturtle()
border_pen.speed(0)
border_pen.pensize(5)
border_pen.color("lime")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
for side in range(4):
    border_pen.forward(600)
    border_pen.left(90)
    
border_pen.hideturtle()

score=0
score_pen=turtle.Turtle()
score_pen.hideturtle()
score_pen.speed(0)
score_pen.pensize(140)
score_pen.color("green")
score_pen.penup()
score_pen.setposition(-290,260)
score_string="SCORE:%s"%score
score_pen.write(score_string,font=("Arial",24,"normal"))
score_pen.hideturtle()


#히어로
turtle.register_shape('yurei.gif')
hero=turtle.Turtle()
hero.hideturtle()
hero.shape('yurei.gif')
hero.penup()
hero.speed(0)
hero.setposition(0,-250)
hero.showturtle()


    
#적만들기
import random
turtle.register_shape('MYGMAE.gif')
numEnemies=10
enemies=[]
for i in range(numEnemies):
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy.hideturtle()
    enemy.speed(0)
    enemy.shape('MYGMAE.gif')
    x=random.randint(-200,200)
    y=random.randint(100,250)
    enemy.setposition(x,y)
    enemy.showturtle()
    
#총알 만들기
bullet=turtle.Turtle()
bullet.hideturtle()
bullet.speed(0)
bullet.color('yellow')
bullet.shape('circle')
bullet.penup()
bullet.shapesize(0.8,0.2)
#bullet.showturtle()

#움직임 정의
import math
def isCollision(t1,t2):
    x1,y1=t1.xcor(),t1.ycor()
    x2,y2=t2.xcor(),t2.ycor()
    distance=math.sqrt((x1-x2)**2+(y1-y2)**2)
    print(distance)
    return True if distance<15 else False 
heroSpeed=5
def moveLeft():
    x=hero.xcor()
    x-=heroSpeed
    if x<-280: x=-280
    hero.setx(x)
    

def moveRight():
    x=hero.xcor()
    x+=heroSpeed
    if x>280: x=280
    hero.setx(x)
    

bulletState='ready'
def fireBullet():
    global bulletState
    if bulletState=='ready':
        bulletState='fire'
        x=hero.xcor()
        y=hero.ycor()+10
        bullet.setposition(x,y)
        bullet.showturtle()

        


turtle.onkeypress(moveLeft,'Left')
turtle.onkeypress(moveRight,'Right')
turtle.onkey(fireBullet,'space')
turtle.listen()

#적의 움직임
enemySpeed=2
bulletSpeed=50
while True:
    for enemy in enemies:
        x=enemy.xcor()
        x+=enemySpeed
        enemy.setx(x)
        if x>280 or x<-280:
            for e in enemies:
                y=e.ycor()
                y-=40
                e.sety(y)
            enemySpeed*=-1
        
    #총알그리기
    if bulletState=='fire':
        y=bullet.ycor()
        y+=bulletSpeed
        bullet.sety(y)
        if y>275:
            bullet.hideturtle()
            bulletState='ready'
            
    for enemy in enemies:
        if isCollision(bullet,enemy):
            bullet.hideturtle()
            bulletState='ready'
            bullet.setposition(0,-400)
            enemy.hideturtle()
            enemies.remove(enemy)
            
            #x=random,randint(-200,200)
            #y=random,randint(100,250)
            #enemy.setposition(x,y)
            score+=10
            scoreString='SCORE:%s'%score
            score_pen.clear()
            score_pen.write(scoreString)
            
         
        if isCollision(hero,enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break
        
            
            
        
        

turtle.mainloop()

