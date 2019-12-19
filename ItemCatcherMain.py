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
import random
import time
#importerer alt ekstra spillet vil trenge for å fungere


FPS=24


WIDTH=750
HEIGHT=750
#lager to variabler for høyde og bredde


pygame.init()
#starter pygame

screen=pygame.display.set_mode((WIDTH, HEIGHT))
#setter inn størrelsene WIDTH og HEIGHT for spillet
pygame.display.set_caption('MinecraftCatcher')
#definerer navn for spillet


clock=pygame.time.Clock()

pygame.display.update()


#this is a new comment


kiste=getworkingpath()+"/rsz_minecraftchest.png"
#henter bildet av kisten fra filplassering på pcen
#kisten er 170 piksler bred og 105 piksler høykjkjhgugyillgiyiyggiygyiigyii
positiv1 = getworkingpath()+"/Diamondpickaxe.png"
positiv2 = getworkingpath()+"/Diamondsword.png"
negativ1 = getworkingpath()+"/rottenflesh.png"
negativ2 = getworkingpath()+"/rottenpotato.png"
#henter bildet av objektene som skal falle fra filplassering på pcen

kistex = 325
kistey = 500

positiv1_x = random.randint(10, WIDTH-60)
positiv1_y = random.randint(-200, 10)

positiv2_x = random.randint(10, WIDTH-60)
positiv2_y = random.randint(-200, 10)

negativ1_x = random.randint(10, WIDTH-60)
negativ1_y = random.randint(-200, 10)

negativ2_x = random.randint(10, WIDTH-60)
negativ2_y = random.randint(-200, 10)
#variablene over er til for å definere hvilken x og y verdi objektene skal ha.
#dette blir implimentert i while loopen. Kiste x og y er mindre komplisert 
#fordi kisten skal starte på samme sted hver gang
objekter = []
muligheter = [positiv1, positiv2, negativ1, negativ2]
 
"""def spawn_objekter():
    a = random(muligheter)
    xpos = random(10, WIDTH-60)
    ypos = 10*yspeed
    screen.blit(a, (xpos, ypos))
    objekter.append(ypos)"""
items = positiv1, positiv2, negativ1, negativ2     
yspeed=8

skrift=pygame.font.Font(None, 80)
def restart():
    skrift = hm.render('Restart', 13, (0,0,0))
    skriftx=WIDTH/2
    skrifty=HEIGHT/2 
    draw.rect(150,150,150)
     
         




#lager variabel for farten til objektene
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if x >= skriftx - 5 and x <= skriftx + textx_size + 5:
                if y >= skrifty - 5 and y <= skrifty + texty_size + 5:
                    in_main_menu = False
                    break

            #for løkken gjør det mulig å lukke spillet på en god måte
            
    screen.fill(pygame.Color("lightblue"))
    #bakgrunnsfarge
    clock.tick(FPS)
    #implimenterer FPS som er definert i starten av koden
    

    dropper1=pygame.image.load(positiv1)
    screen.blit(dropper1, (positiv1_x, positiv1_y))
    dropper2=pygame.image.load(positiv2)
    screen.blit(dropper2, (positiv2_x, positiv2_y))
    #dropper er positve items. Dropper1 og 2 gjør at sverdet og hakken
    #spawner innenfor x = (10, WIDTH-60)) og y = 10

    hopper1=pygame.image.load(negativ1)
    screen.blit(hopper1, (negativ1_x, negativ1_y))
    hopper2=pygame.image.load(negativ2)
    screen.blit(hopper2, (negativ2_x, negativ2_y))
    #hopper er negative items. Hopper1 og 2 gjør at poteten og kjøttet spawner 
    #innenfor x = (10, WIDTH-60)) og y = 10
    
    
    """if positiv1_y>=kistey and positiv1_x<=kistex or positiv2_y >= kistey+5: yspeed = 0"""
    #if negativ1_y or negativ2_y == 505: 
    
    """a=positiv1_y"""
    a=positiv1_y
    b=positiv2_y
    c=negativ1_y
    d=positiv2_y
    if a>HEIGHT:
        positiv1_y = random.randint(-200, 10)
        positiv1_x = random.randint(10, WIDTH-60)
    if b>HEIGHT:
        positiv2_y = random.randint(-200, 10)
        positiv2_x = random.randint(10, WIDTH-60)
    if c>HEIGHT:
        negativ1_y = random.randint(-200, 10)
        negativ1_x = random.randint(10, WIDTH-60)
    if d>HEIGHT:
        negativ2_y = random.randint(-200, 10)
        negativ2_x = random.randint(10, WIDTH-60)  
    #på denne måten vil objektene respawne hvis de går ut av skjermen
    #if positiv1.contains(kiste):
    #    crash
                    
    

    boks=pygame.image.load(kiste)
    screen.blit(boks, (kistex, kistey))
    keys=pygame.key.get_pressed() 
    if 0<=kistex<=750:
        #lager en if funksjon for x verdiene mellom 0 og 750
        
        if keys[K_LEFT]:
            kistex-= 10
            #når venstre piltast er nede går kisten 10 piksler til venstre
        if keys[K_RIGHT]:
            kistex+=10
            #når høyre piltast er nede går kisten 10 piksler til høyre
        if kistex<=0:
            kistex+=10
        if kistex>=580:
            kistex-=10
            #kistex og y er kun lik +10 og -10 dersom kisten er innenfor 
            #x-verdiene 0 og 580. (Kisten er 170 piksler bred) Slik kan ikke
            #kisten gå ut av skjermen
    
    positiv1_y+=yspeed
    positiv2_y+=yspeed
    negativ1_y+=yspeed
    negativ2_y+=yspeed
    #gjør at objektene faller
    pygame.display.update()
    pygame.display.flip()
   
    
"""K_UP        up arrow
K_DOWN                down arrow
K_RIGHT               right arrow
K_LEFT                left arrow
    
pygame.draw.rect(screen, (0,200,0), (x,y,10, 10), 0) 
 
    if e.key == pygame.K_LEFT:
        Bakgrunn
    For lyd, add linjen under
    pygame.mixer.init()
    
if e.type == pygame.KEYDOWN: #dersom vi trykker en tast
            screen.blit(kiste, (kistex, kistey))
            pygame.display.update()
            if e.type == pygame.K_LEFT: #dersom tasten er venstrepil
                kistex = kistex - 10
            if e.type == pygame.QUIT: 
                pygame.quit()
        keys=pygame.key.get_pressed()"""
        



