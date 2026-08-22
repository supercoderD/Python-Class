import pygame
pygame.init()
screenwidth,screenheight=500,500
screen=pygame.display.setmode((screenwidth,screenheight))
pygame.display.setcaption("Adding image and background image.") 
backgroundimage=pygame.transform.scale
(pygame.image.load
("istockphoto.png").convert(),(screenwidth,screenheight))
guyimage=pygame.trasform.scale(pygame.image.load("guy.png").convert_alpha(),(200,200))
guyrect=guyimage.get_rect(center=(screenwidth//2,screenheight//2-30))

# done=False
# while not done:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT():
#             pygame.quit()
#     pygame.display.flip()
def gameloop():
    clock=pygame.time.clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        screen.blit(backgroundimage, (0,0))
        screen.blit(guyimage, guyrect)
        pygame.display.flip()

        clock.tick=(60)
    pygame.quit

if __name__=="__main__":
    gameloop()
#install 3.13/3.12 python pip and uninstall 3.14 or 3.9.
#for pygame module to be installed.




