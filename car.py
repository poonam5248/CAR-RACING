import pygame
from pygame import *
import os

pygame.init()

(length,height)=(600,600)

black =(0,0,0)
white =(255,255,255)
red =(255,0,0)

window=display.set_mode((length,height))
display.set_caption(" car racing")
display.flip()

carimg = image.load('download.png')

def gam_loop():
    x = (length * 0.42)
    y = (height *0.72)
    move = 0
    def car(x,y):
        window.blit(carimg,(x,y))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move= -1
                elif event.key == pygame.K_RIGHT:
                    move = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    move = 0

        x += move
        window.fill(white)
        car(x,y)
        display.flip()

gam_loop()
pygame.quit()
