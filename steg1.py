# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 10:17:11 2019

@author: jorgeh1411
"""

import pygame, sys
from pygame.locals import *

#Frames pr second
FPS=24

#window size
WIDTH=600
HEIGHT=600

#initialize the pygame environment
pygame.init()

# set up the window with size and caption
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('En eller annen tittel her')

# creates a clock
clock=pygame.time.Clock()

while True:
    #limit updates to FPS
    clock.tick(FPS)

    #draw background color to blank the screen
    screen.fill((255,200,200)) #gray background

    #get events from the event queue
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #update display
    pygame.display.flip()
