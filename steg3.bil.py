import pygame, sys
from pygame.locals import *


#style=0 => filled, style=1 => thin line, style=4 => thick line
FILLED=0
FRAMED=1
LINESTYLE=4

#Frames pr second
FPS=40

#window size
WIDTH=800
HEIGHT=500

#initialize the pygame environment
pygame.init()

# set up the window with size and caption
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Framework')

#draw background color to blank the screen
screen.fill((192,192,192))

# creates a clock
clock=pygame.time.Clock()
blink=False

while True:
    #limit updates to FPS
    clock.tick(FPS)

    #get events from the event queue
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.draw.circle(screen, (0,170,170), (525, 275), 18, FILLED)
    """if blink:
        blink=false
else:
    blink=True
    blink=not blink"""
    

    #rect(screen, color, coords(top, left, width, height), fillstyle
    pygame.draw.rect(screen, (YELLOW), (175, 200, 350, 150), FILLED)
    pygame.draw.rect(screen, (255,255,0), (175, 200, 350, 150), FILLED)
    pygame.draw.circle(screen, (0,0,0), (175, 350), 40, FILLED)
    pygame.draw.circle(screen, (0,0,0), (525, 350), 40, FILLED)

    #update display
    pygame.display.flip()
