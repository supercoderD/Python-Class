import pygame
import random
pygame.init()
spritecolorchangeevent=pygame.USEREVENT+1
backgroundcolorchangeevent=pygame.USEREVENT+2
blue=pygame.Color("blue")
lightblue=pygame.Color("lightblue")
red=pygame.Color("red")
yellow=pygame.Color("yellow")

orange=pygame.Color("orange")
white=pygame.Color("white")
green=pygame.Color("green")
purple=pygame.Color("purple")

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.velocity=[random.choice([-1,1]),random.choice([-1,1])]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundaryhit=False
        if self.rect.left <=0 or self.rect.right >=500:
            self.velocity[0]=self.velocity[0]
            boundaryhit=True
        if self.rect.top <=0 or self.rect.bottom >=400:
            self.velocity[1]=self.velocity[1]
            boundaryhit=True
        if boundaryhit:
            pygame.event.post(pygame.event.Event(spritecolorchangeevent))
            pygame.event.post(pygame.event.Event(backgroundcolorchangeevent))

    def changecolor(self):
        self.image.fill(random.choice([blue,red,yellow,lightblue]))

def changebackground():
    global bgcolor
    bgcolor=random.choice([orange,white,green,purple])

allspriteslist=pygame.sprite.Group()
sprite1=Sprite(white,20,30)
sprite1.rect.x=random.randint(0,480)
sprite1.rect.y=random.randint(0,370)
allspriteslist.add(sprite1)
screen=pygame.display.set_mode((700,600))
pygame.display.set_caption("Colorful Bounce")
bgcolor=white
screen.fill(bgcolor)
exit=False
clock=pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit=True
        elif event.type==spritecolorchangeevent:
            sprite1.changecolor()
        elif event.type==backgroundcolorchangeevent:
            changebackground()
    allspriteslist.update()
    screen.fill(bgcolor)
    allspriteslist.draw(screen)
    pygame.display.flip()
    clock.tick(200)

pygame.quit()









