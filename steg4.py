import pygame, sys
from pygame.locals import *

#line thickness
LINESTYLE=2

#Frames pr second
FPS=20

#window size
WIDTH=600
HEIGHT=600

#initialize the pygame environment
pygame.init()

# set up the window with size and caption
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Lines')

#draw background color to blank the screen
screen.fill((0,0,0))

# creates a clock
clock=pygame.time.Clock()

while True:
    #limit updates to FPS
    clock.tick(FPS)

    #get events from the event queue
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #line(screen, color, coords1(x, y), coords2(x, y), fillstyle
    pygame.draw.line(screen, (255,0,255), (100, 100), (150, 200), LINESTYLE)

    #update display
    pygame.display.flip()
