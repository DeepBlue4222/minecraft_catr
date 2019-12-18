#haunted house
import pygame, sys
from pygame.locals import *
import random
from getworkingpath import *


#construct the sound filename
fileSound1=getworkingpath()+"/hauntedhouse.wav"
fileSound2=getworkingpath()+"/fakenews1.wav"

#construct the picture filename
filePicture=getworkingpath()+"/trump.png"

#Frames pr second
FPS=24

#style=0 => filled, style=1 => thin line, style=4 => thick line
FILLED=0

#window size
WIDTH=700
HEIGHT=400

#initialize the pygame environment
pygame.init()

#sound engine
pygame.mixer.init()

#load the picture
trump=pygame.image.load(filePicture)

# set up the window with size and caption
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hus')

# creates a clock
clock=pygame.time.Clock()

#define the the location and sise of the door
door=Rect(325, 220, 40, 80)
#current door state
dooropenclose=True

while True:
    #limit updates to FPS
    clock.tick(FPS)

    #get events from the event queue
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #check if something happens wth the mouse
        elif event.type == MOUSEBUTTONUP:
            #get mouse position
            posx,posy=event.pos
            #did you click on the door
            if door.collidepoint(posx, posy):
                #toggle door state
                dooropenclose=not dooropenclose

                if dooropenclose:
                    #load sound
                    pygame.mixer.music.load(fileSound2)
                else:
                    #load sound
                    pygame.mixer.music.load(fileSound1)
                #play sound
                pygame.mixer.music.play()

    #draw background color to blank the screen
    screen.fill(pygame.Color("gray")) #grey background

    #ground floor
    pygame.draw.rect(screen, pygame.Color("blue"), (200,200,250,100), 0)

    #chimney
    pygame.draw.rect(screen, pygame.Color("brown"), (375, 150, 30, 40), 0)

    #roof
    polygons=[(200,200),(325,150),(450,200)]
    pygame.draw.polygon(screen, pygame.Color("yellow"), polygons, 0)

    #togle color of door
    doorcolor=pygame.Color("red")
    if not dooropenclose:
        doorcolor=pygame.Color("black")

    #door
    pygame.draw.rect(screen, doorcolor, door, 0)

    if dooropenclose:
        #sun
        pygame.draw.circle(screen, pygame.Color("yellow"), (WIDTH-60, 60), 50)
    else:
        #draw the trump
        screen.blit(trump, (WIDTH-105,15))
    
    #window
    pygame.draw.rect(screen, pygame.Color("white"), (255,255,30,30), 0)
    pygame.draw.rect(screen, pygame.Color("white"), (220,255,30,30), 0)
    pygame.draw.rect(screen, pygame.Color("white"), (255,220,30,30), 0)
    pygame.draw.rect(screen, pygame.Color("white"), (220,220,30,30), 0)

    #grass
    for x in range(0, WIDTH, 10):
        pygame.draw.line(screen, pygame.Color("green"), (x, 300), (x, 320), 4)

    #tree
    pygame.draw.rect(screen, pygame.Color("brown"), (550, 250, 20,50), 0)
    pygame.draw.circle(screen, pygame.Color("green"), (550,245), 10)
    pygame.draw.circle(screen, pygame.Color("green"), (540,245), 10)
    pygame.draw.circle(screen, pygame.Color("green"), (550,250), 10)
    pygame.draw.circle(screen, pygame.Color("green"), (560,245), 10)
    pygame.draw.circle(screen, pygame.Color("green"), (555,255), 10)
    pygame.draw.circle(screen, pygame.Color("green"), (565,255), 10)

    #update display
    pygame.display.flip()