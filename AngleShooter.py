# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 08:16:48 2019

@author: jorgeh1411
from pygame.locals import *
from getworkingpath import *
"""

import pygame, sys
from pygame.locals import *
from getworkingpath import *



FILLED=0



FPS=40


WIDTH=750
HEIGHT=750
"""importer png. Gjør kisten flyttbar med piltaster"""

pygame.init()

pygame.mixer.init()


screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('ItemCatcher')
screen.fill(pygame.Color("lightblue"))

clock=pygame.time.Clock()

pygame.display.update()

kiste = pygame.image.load("rsz_minecraftchest.png")
kistex = 325
kistey = 500

screen.blit(kiste, (kistex, kistey)) #posisjon til kiste
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill(pygame.Color("lightblue"))
    #limit updates to FPS
    clock.tick(FPS)
    screen.blit(kiste, (kistex, kistey))
    keys=pygame.key.get_pressed()   
    if keys[pygame.K_LEFT]:
        kistex-= 10
    if keys[pygame.K_RIGHT]:
        kistex+= 10
    
    pygame.display.update
    
    pygame.display.update()
    pygame.display.flip()
    clock=pygame.time.Clock()
    
    
"""K_UP        up arrow
K_DOWN                down arrow
K_RIGHT               right arrow
K_LEFT                left arrow
    
pygame.draw.rect(screen, (0,200,0), (x,y,10, 10), 0) 
 
    if e.key == pygame.K_LEFT:
        Bakgrunn
    
    
if e.type == pygame.KEYDOWN: #dersom vi trykker en tast
            screen.blit(kiste, (kistex, kistey))
            pygame.display.update()
            if e.type == pygame.K_LEFT: #dersom tasten er venstrepil
                kistex = kistex - 10
            if e.type == pygame.QUIT: 
                pygame.quit()
        keys=pygame.key.get_pressed()"""



