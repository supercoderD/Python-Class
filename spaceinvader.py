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






