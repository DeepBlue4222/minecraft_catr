import pygame, sys
from pygame.locals import *
import random 

#Frames pr second
FPS=24

#style=0 => filled, style=1 => thin line, style=4 => thick line
FILLED=0

#window size
WIDTH=600
HEIGHT=600

#initialize the pygame environment
pygame.init()

# set up the window with size and caption
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('En eller annen tittel her')


"""to=random.randint(1,100)"""
screen.fill((192,192,192)) 

# creates a clock
clock=pygame.time.Clock()

while True:
    #limit updates to FPS
    clock.tick(FPS)
    x=random.randint(0,WIDTH)
    y=random.randint(0,HEIGHT)
    a=random.randint(1,100)
    #draw background color to blank the screen
    #gray background

    #get events from the event queue
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #circle(screen, color, coords(x, y), radius, fillstyle
    pygame.draw.circle(screen, (255,0,0), (x, y), (a), FILLED)
    
    
    """pygame.draw.rect(screen, (YELLOW), (175, 200, 350, 150), FILLED)"""

    #update display
    pygame.display.flip()
