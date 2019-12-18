import pygame, sys
from pygame.locals import *

#Frames pr second
FPS=24

#window size
WIDTH=800
HEIGHT=500

#initialize the pygame environment
pygame.init()

# set up the window with size and caption
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Framework')

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

    #polygon(screen, color, pointlist((x, y)...), fillstyle
    pointlist_1 = [(25, 25), (105, 185), (185, 25)]
    pygame.draw.polygon(screen, (0,255,0), pointlist_1, 2)

    #update display
    pygame.display.flip()
