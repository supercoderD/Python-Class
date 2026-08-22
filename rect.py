# import pygame
# pygame.init()
# screen=pygame.display.set_mode((500,500))
# screen.fill((255,255,255))
# done=False
# while not done:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             done=True
#     pygame.draw.rect(screen, ("Lime Green"), pygame.Rect(40,40,80,100))
#     pygame.draw.circle(screen,("Lime Green"),(300,00),(100))
#     pygame.draw.circle(screen,("Lime Green"),(200,300),(100), 6)

#     pygame.display.flip()












import pygame
def main():
    pygame.init()
    screenwidth, screenheight=500,500
    screen=pygame.display.set_mode((screenwidth,screenheight))
    pygame.display.set_caption("color changing sprite")

    colors={"red":pygame.Color("red"),
        "yellow":pygame.Color("yellow"),
        "green":pygame.Color("green"),
        "blue":pygame.Color("blue"),
        "white":pygame.Color("white")}
    currentcolor=colors["white"]
    x,y=30,30
    spritewidth,spriteheight=60,60
    clock=pygame.time.Clock()
    done=False
    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True
        pressed=pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:x-=3
        if pressed[pygame.K_RIGHT]:x+=3
        if pressed[pygame.K_UP]:y-=3
        if pressed[pygame.K_DOWN]:y+=3

        x=min(max(0,x),screenwidth-spritewidth)
        y=min(max(0,y),screenheight-spriteheight)
        if x==0: currentcolor=colors["blue"]
        elif x==screenwidth-spritewidth:currentcolor=colors["yellow"]
        elif y==0: currentcolor=colors["red"]
        elif y== screenheight-spriteheight: currentcolor=colors["green"]
        screen.fill((0,0,0))
        pygame.draw.rect(screen,currentcolor,(x,y,spritewidth,spriteheight))
        pygame.display.flip()
    pygame.quit()

if __name__=="__main__":
    main()
