# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 08:26:33 2019

@author: jorgeh1411
"""


import pygame, sys
from pygame.locals import *
from getworkingpath import *
"""import time """

lydfil=getworkingpath()+ "pierre.waw"

#style=0 => filled, style=1 => thin line, style=4 => thick line
FILLED=0
FILLED2=4
FRAMED=1
LINESTYLE=4

#Frames pr second
FPS=40

#window size
WIDTH=800
HEIGHT=500
   
#initialize the pygame environment
pygame.init()

pygame.mixer.init()

# set up the window with size and caption
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Yo Pierre')

color =(192,192,192) 
#draw background color to blank the screen
screen.fill(color)

door=pygame.Rect(376,300,40,50)
doc=True
# creates a clock
clock=pygame.time.Clock()
blink=False

while True:
    screen.fill(color)
    #limit updates to FPS
    clock.tick(FPS)
    polygonliste=[(325,250), (450,195), (575,250)]

    #get events from the event queue
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == MOUSEBUTTONDOWN:
            posx,posy=event.pos
            if door.collidepoint(posx,posy):
                doc = not doc
""" pygame.mixer.music.load(lydfil)
pygame.mixer.music.play() """

                
                
                
            
    doorColor=pygame.Color(255,255,0)
    if doc == False:
       doorColor=pygame.Color(0,0,0)
    pygame.draw.rect(screen, (0,0,255), (0,0,800,350),0)
    pygame.draw.rect(screen, (255,0,0), (345,250,210,100),0)
    pygame.draw.rect(screen, (0,0,0), (475,290,70,60),0)
    pygame.draw.rect(screen, doorColor, (376,300,40,50),0)
    
    
    for g in range(0,WIDTH, 10):
        pygame.draw.line(screen, (0,255,0), (g,350), (g,500), FILLED2)
    pygame.draw.polygon(screen,(255,255,0), polygonliste, FILLED)
    


    #update display
pygame.display.flip()