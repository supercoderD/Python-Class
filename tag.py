import pygame
import random
screenwidth,screenheight=500,400
movementspeed=5
fontsize=100
pygame.init()
font=pygame.font.Sysfont("Times", fontsize)
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(pygame.Color("limegreen"))
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
        self.rect=self.image.get_rect()
    def move(self,xchange,ychange):
        self.rect.x=max(min(self.rect.x+xchange,screenwidth-self.rect.width),0)
        self.rect.y=max(min(self.rect.y+ychange,screenheight-self.rect.height),0)
screen=pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption("Sprite Tag")
allsprites=pygame.sprite.Group()
sprite1=Sprite(pygame.color("black"),20,30)
sprite1.rect.x=random.randint(0,screenwidth-sprite1.rect.width)
sprite1.rect.y=random.randint(0,screenheight-sprite1.rect.height)
allsprites.add(sprite1)
sprite2=Sprite(pygame.color("red"),20,30)
sprite2.rect.x=random.randint(0,screenwidth-sprite2.rect.width)
sprite2.rect.y=random.randint(0,screenheight-sprite2.rect.height)
allsprites.add(sprite2)
running,sprite1won,sprite2won=True,False,False
clock=pygame.time.Clock()
sprite1points=0
sprite2points=0
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_x):
            running=False
    if not sprite1won or sprite2won:
        keys=pygame.key.get_pressed()
        xchange=(keys[pygame.K_RIGHT]-keys[pygame.K_LEFT])*movementspeed
        ychange=(keys[pygame.K_DOWN]-keys[pygame.K_UP])*movementspeed
        sprite1.move(xchange,ychange)
        scorefont=pygame.font.SysFont("Arial",36)
        if sprite1.rect.colliderect(sprite2.rect):
            sprite1points+=1
        if sprite2.rect.colliderect(sprite1.rect):
            sprite2points+=1
        if sprite1points==10:
            sprite1won=True
        if sprite2points==10:
            sprite2won=True
allsprites.draw(screen)
scoretext=scorefont.render(f"Score for sprite1{sprite1points})","Score for sprite2 points{sprite2points}",True,pygame.Color("black"))
screen.blit(scoretext,(xchange,ychange))
if sprite1won:
    sprite1wintext=font.render("sprite1 wins!",True,pygame.color("black"))
    screen.blit(sprite1wintext,((screenwidth-sprite1wintext.get_width())//2,(screenheight-sprite1wintext.get_height())//2))
if sprite2won:        
    sprite2wintext=font.render("sprite2 wins!",True,pygame.color("black"))
    screen.blit(sprite2wintext,((screenwidth-sprite2wintext.get_width())//2,(screenheight-sprite2wintext.get_height())//2))
pygame.display.flip()
clock.tick(90)
pygame.quit()

        

