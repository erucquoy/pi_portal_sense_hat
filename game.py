# Portal game with SenseHat on Raspberry Pi - Rucquoy Edouard
from sense_hat import SenseHat
import os
import time
import pygame
from pygame.locals import *
from random import randint


sense = SenseHat() # Init SenseHat
sense.clear() # Clear matrix
pygame.init() # Init pygame

# Declaration de l'affichage 
# (obligatoire pour gestion des touches/joystick)
pygame.display.set_mode((1, 1))


# Random place for Blue & Orange portals
x_blue = randint(1,6)
y_blue = randint(1,6)

x_red = randint(1,6)
y_red = randint(1,6)

# Init white player
x_white = 0;
y_white = 0;

# Init colors
red = (255, 128, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

# Init game
sense.set_pixel(x_blue, y_blue, blue)
sense.set_pixel(x_red, y_red, red)
sense.set_pixel(x_white, y_white, white)

# Fonction de gestion des actions en fonction des touches
def handle_event(event):
    global y_white
    global x_white
    global y_blue
    global x_blue
    global y_red
    global x_red
    global black
    global white
    if event.key == pygame.K_DOWN:
	    if y_white < 7:
            if (y_blue == y_white+1) and (x_blue == x_white):
                sense.set_pixel(x_white, y_white, black)
                y_white = y_red+1
                x_white = x_red
                sense.set_pixel(x_white, y_white, white)
            elif (y_red == y_white+1) and (x_red == x_white):
                sense.set_pixel(x_white, y_white, black)
                y_white = y_blue+1
                x_white = x_blue
                sense.set_pixel(x_white, y_white, white)
            else:
                sense.set_pixel(x_white, y_white, black)
            y_white = y_white + 1
            sense.set_pixel(x_white, y_white, white)

    elif event.key == pygame.K_UP:
        if y_white > 0:
            if (y_blue == y_white-1) and (x_blue == x_white):
                sense.set_pixel(x_white, y_white, black)
                y_white = y_red-1
                x_white = x_red
                sense.set_pixel(x_white, y_white, white)
            elif (y_red == y_white-1) and (x_red == x_white):
                sense.set_pixel(x_white, y_white, black)
                y_white = y_blue-1
                x_white = x_blue
                sense.set_pixel(x_white, y_white, white)
            else:
                sense.set_pixel(x_white, y_white, black)
            y_white = y_white - 1
            sense.set_pixel(x_white, y_white, white)

    elif event.key == pygame.K_LEFT:
        if x_white < 7:
            if (x_blue == x_white-1) and (y_white == y_blue):
                sense.set_pixel(x_white, y_white, black)
                x_white = x_red-1
                y_white = y_red
                sense.set_pixel(x_white, y_white, white)
            elif (x_red == x_white-1) and (y_white == y_red):
                sense.set_pixel(x_white, y_white, black)
                x_white = x_blue-1
                y_white = y_blue
                sense.set_pixel(x_white, y_white, white)
            else:
                sense.set_pixel(x_white, y_white, black)
                x_white = x_white - 1
                sense.set_pixel(x_white, y_white, white)
    elif event.key == pygame.K_RIGHT:
        if x_white > 0:
            if (x_blue == x_white+1) and (y_white == y_blue):
                sense.set_pixel(x_white, y_white, black)
                x_white = x_red+1
                y_white = y_red
                sense.set_pixel(x_white, y_white, white)
            elif (x_red == x_white+1) and (y_white == y_red):
                sense.set_pixel(x_white, y_white, black)
                x_white = x_blue+1
                y_white = y_blue
                sense.set_pixel(x_white, y_white, white)
            else:
                sense.set_pixel(x_white, y_white, black)
                x_white = x_white + 1
                sense.set_pixel(x_white, y_white, white)
    elif event.key == pygame.K_RETURN:
        pass

# Variable (jeu en cours de fonctionnement ou stoppé)
running = True

# Boucle du jeu
while running:
	pygame.event.pump()
    	for event in pygame.event.get():
        	if event.type == pygame.QUIT:
            		running = False
        	if event.type == KEYDOWN:
            		if event.key == K_ESCAPE:
                		running = False
            		handle_event(event)
