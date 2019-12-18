# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 10:04:50 2019

@author: jorgeh1411
"""

import pygame, sys
from pygame.locals import *
FPS = 24
WIDHT=500
HEIGHT=500

clock=pygame.time.Clock()
while True: 
    clock.tick(FPS)
    screen.fill((177,0,0))