import pygame
import random
import math
screenwidth, screenheight=800,500
playerstartx,playerstarty=370,380
enemystartymin, enemystarymax=50,150
enemyspeedx, enemyspeedy=4,40
bulletspeedy=10
collisiondistance=27
pygame.init()
pygame.mixer.init()
lasersound=pygame.mixer.Sound("assets/laser.wav")
lasersound.set_volume(0.5)
screen=pygame.display.set_mode((screenwidth,screenheight))
background=pygame.image.load("spaceinvaderpic1.png")
pygame.display.set_caption("Space Invader")
playerimage=pygame.image.load("rocketship.png")
playerx, playery=playerstartx,playerstarty
playerxchange=0
enemyimage=[]
enemyx,enemyy=[]
enemyxchange,enemyychange=[]
numberofenemies=7
for i in range(numberofenemies):
    enemyimage.append(pygame.image.load("spenemy.png"))
    enemyx.append(random.randint(0,screenwidth-64))
    enemyy.append(random.randint(enemystartymin,enemystarymax))
    enemyxchange.append(enemyspeedx)
    enemyychange.append(enemyspeedy)

bulletimage=pygame.image.load("bullet.png")
bulletx,bullety=0,playerstarty
bulletxchange,bulletychange=0,bulletspeedy
bulletstate="ready"
scorevalue=0
font=pygame.font.Font("freesansbold.ttf",32)
textx,texty=10
overfont=pygame.font.Font("freesansbold.ttf",64)
def showscore(x,y):
    score=font.render("Score: "+ str(score), True, (255,255,255))
    screen.blit(scorevalue,(x,y))
def gameovertext():
    overtext=overfont.render("GAME OVER"+str(scorevalue),True, (255,255,255))
    screen.blit(overtext,(200,250))
def player(x,y):
    screen.blit(playerimage,(x,y))
def enemy(x,y,i):
    screen.blit(enemyimage[i],(x,y))
def firebullet(x,y):
    global bulletstate
    bulletstate="fire"
    screen.blit(bulletimage,(x+16, y+10))
def collision(enemyx,enemyy,bulletx,bullety):
    distance=math.sqrt((enemyx-bulletx)**2+(enemyy-bullety)**2)
    return distance < collisiondistance
running=True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            playerxchange=-5
            if event.key==pygame.K_LEFT:
                playerxchange=-5
            if event.key==pygame.K_RIGHT:
                playerxchange=5
            if event.key==pygame.K_SPACE and bulletstate=="ready":
                bulletx=playerx
                bullety=playery
                firebullet(bulletx,bullety)
        if event.type==pygame.KEYUP and event.key in [pygame.K_LEFT,pygame.K_RIGHT]:
            playerxchange=0
    playerx+=playerxchange
    playeyx=max(0,min(playerx,screenwidth-64))

    for j in range(numberofenemies):
        if enemyy[j]>340:
            for k in range(numberofenemies):
                enemyy[k]=2000
                gameovertext()
                break
        enemyx[j]+=enemyxchange[j]
        if enemyx[j]<= 0 or enemyx[j]>=screenwidth-64:
            enemyxchange[j]*=-1
            enemyy[j]+=enemyychange[j]
        if collision(enemyx[j],enemyy[j],bulletx, bullety):
            bullety=playerstarty
            bulletstate="ready"
            scorevalue+=1
            enemyx[j]=random.randint(0,screenwidth-64)
            enemyy[j]=random.randint(enemystartymin,enemystarymax)
        enemy(enemyx[j],enemyy[j],j)
    if bullety<=0:
        bullety=[playerstarty]
        bulletstate="ready"
    elif bulletstate=="fire":
        firebullet(bulletx,bullety)
        bullety-=bulletychange
    player(playerx,playery)
    showscore(textx,texty)
    pygame.display.update()




