# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 08:16:48 2019

@author: jorgeh1411
from pygame.locals import *
from getworkingpath import *
"""

import pygame
import sys
from pygame.locals import *
from getworkingpath import *
import random
import time

# importerer alt ekstra spillet vil trenge for å fungere


FPS = 24


WIDTH = 750
HEIGHT = 750
# lager to variabler for høyde og bredde


pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
# starter pygame

screen = pygame.display.set_mode((WIDTH, HEIGHT))
# setter inn størrelsene WIDTH og HEIGHT for spillet
pygame.display.set_caption('MinecraftCatcher')
# definerer navn for spillet


clock = pygame.time.Clock()

pygame.display.update()



#this is a new comment


kiste=getworkingpath()+"/rsz_minecraftchest.png"
#henter bildet av kisten fra filplassering på pcen
#kisten er 170 piksler bred og 105 piksler høykjkjhgugyillgiyiyggiygyiigyii

kiste = getworkingpath()+"/rsz_minecraftchest.png"
# henter bildet av kisten fra filplassering på pcen
# kisten er 170 piksler bred og 105 piksler høykjkjhgugyillgiyiyggiygyiigyii

hakke = getworkingpath()+"/Diamondpickaxe.png"
sverd = getworkingpath()+"/Diamondsword.png"
kjøtt = getworkingpath()+"/rottenflesh.png"
potet = getworkingpath()+"/rottenpotato.png"
# henter bildet av objektene som skal falle fra filplassering på pcen

kistex = 325
kistey = 500

hakkex = random.randint(10, WIDTH-60)
hakkey = random.randint(-200, 10)

sverdx = random.randint(10, WIDTH-60)
sverdy = random.randint(-200, 10)

kjøttx = random.randint(10, WIDTH-60)
kjøtty = random.randint(-200, 10)

potetx = random.randint(10, WIDTH-60)
potety = random.randint(-200, 10)
# variablene over er til for å definere hvilken x og y verdi objektene skal ha.
# dette blir implimentert i while loopen. Kiste x og y er mindre komplisert
# fordi kisten skal starte på samme sted hver gang
objekter = []
muligheter = [hakke, sverd, kjøtt, potet]

"""def spawn_objekter():
    a = random(muligheter)
    xpos = random(10, WIDTH-60)
    ypos = 10*yspeed
    screen.blit(a, (xpos, ypos))
    objekter.append(ypos)"""

"""def restart():
    skrift = hm.render('Restart', 13, (0,0,0))
    skriftx=WIDTH/2
    skrifty=HEIGHT/2 
    draw.rect(150,150,150)"""
     

# function to check if two objects collide
# returns boolean

def collide(x1, x2, y1, y2, w1, w2, h1, h2):
    if (x1+w1 > x2 and x1 < x2+w2 and y1+h1 > y2 and y1 < y2+h2):
        return True
    else:
        return False
    
def restart(): 
    boks = pygame.image.load(kiste)
    screen.blit(boks, (kistex, kistey))
    
    
    score = 0
    lives = 0





yspeed=9
score = 0
lives = 3
running = True
# lager variabel for farten til objektene
while running:
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
            

            # for løkken gjør det mulig å lukke spillet på en god måte


    screen.fill(pygame.Color("lightblue"))
    # bakgrunnsfarge
    clock.tick(FPS)
    # implimenterer FPS som er definert i starten av koden

    dropper1 = pygame.image.load(hakke)
    screen.blit(dropper1, (hakkex, hakkey))
    dropper2 = pygame.image.load(sverd)
    screen.blit(dropper2, (sverdx, sverdy))
    # dropper er positve items. Dropper1 og 2 gjør at sverdet og hakken
    # spawner innenfor x = (10, WIDTH-60)) og y = 10

    hopper1 = pygame.image.load(kjøtt)
    screen.blit(hopper1, (kjøttx, kjøtty))
    hopper2 = pygame.image.load(potet)
    screen.blit(hopper2, (potetx, potety))
    # hopper er negative items. Hopper1 og 2 gjør at poteten og kjøttet spawner
    # innenfor x = (10, WIDTH-60)) og y = 10

    boks = pygame.image.load(kiste)
    screen.blit(boks, (kistex, kistey))
    a = hakke
    b = sverd
    c = kjøtt
    d = potet
    

    # check if items collide with chest
    if (collide(hakkex, kistex, a, kistey, dropper1.get_size()[0], boks.get_size()[0], dropper1.get_size()[1], boks.get_size()[1])):
        hakkex = random.randint(-200, 10)
        hakkey = random.randint(10, WIDTH-60)
        score += 10
        

    if (collide(sverdx, kistex, b, kistey, dropper2.get_size()[0], boks.get_size()[0], dropper2.get_size()[1], boks.get_size()[1])):
        sverdy = random.randint(-200, 10)
        sverdx = random.randint(10, WIDTH-60)
        score += 10
        
    if (collide(kjøttx, kistex, c, kistey, hopper1.get_size()[0], boks.get_size()[0], hopper1.get_size()[1], boks.get_size()[1])):
        kjøttx = random.randint(-200, 10)
        kjøtty = random.randint(10, WIDTH-60)
        lives-=1
       

    if (collide(potet, kistex, d, kistey, hopper2.get_size()[0], boks.get_size()[0], hopper2.get_size()[1], boks.get_size()[1])):
        potety = random.randint(-200, 10)
        potetx = random.randint(10, WIDTH-60)
        lives-=1
        
    if lives <= 0:
        text1 = myfont.render(("du tapte") , False, (0, 0, 0))
        screen.blit(text1, (200,200)) #WIDTH/2, HEIGHT/2)
        running = False
    if score >= 200:
        text2 = myfont.render(("Du vant") , False, (0, 0, 0))
        screen.blit(text2, (200,200)) #WIDTH/2, HEIGHT/2)
        running = False
    if a > HEIGHT:
        hakkey = random.randint(-200, 10)
        hakkex = random.randint(10, WIDTH-60)
    if b > HEIGHT:
        sverdy = random.randint(-200, 10)
        sverdx = random.randint(10, WIDTH-60)
    if c > HEIGHT:
        kjøtty = random.randint(-200, 10)
        kjøttx = random.randint(10, WIDTH-60)
    if d > HEIGHT:
        potety = random.randint(-200, 10)
        potetx = random.randint(10, WIDTH-60)
        

   
    # på denne måten vil objektene respawne hvis de går ut av skjermen
    # if positiv1.contains(kiste):
    #    crash skrivv mer utfyllende

    keys = pygame.key.get_pressed()
    if 0 <= kistex <= 750:
        # lager en if funksjon for x verdiene mellom 0 og 750

        if keys[K_LEFT]:
            kistex -= 10
            # når venstre piltast er nede går kisten 10 piksler til venstre
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
    text3 = myfont.render(("score: " + str(score)) , False, (0, 0, 0))
    screen.blit(text3, (0, 0))
    text4 = myfont.render(("lives left: " + str(lives)) , False, (0, 0, 0))
    screen.blit(text4, (0, 50))
   
    
    hakkey+=yspeed
    sverdy+=yspeed
    kjøtty+=yspeed
    potety+=yspeed
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
