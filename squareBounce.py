import pygame, sys, time
from pygame.locals import *

# set up pygame
pygame.init()

# set up window
window = pygame.display.set_mode((700, 500))
pygame.display.set_caption('Square Bounce!') 

 # set up the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
windowSurface.fill(white)