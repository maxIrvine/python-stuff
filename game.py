import pygame, sys, time
from pygame.locals import *

# set up pygame
pygame.init()

# set up window
windowSurface = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Hello world!') 

 # set up the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
windowSurface.fill(white)

# shapes and stuff!

#main game loop
while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
    pygame.draw.circle(windowSurface, green, (300, 50+count), 20, 0)
    time.sleep(1)
    count = count + 1
        
        pygame.display.update()

# # set up fonts
# basicFont = pygame.font.SysFont(None, 48)

# # set up text
# text = basicFont.render('Hello world!', True, white, blue)
# textRect = text.get_rect()
# textRect.centerx = windowSurface.get_rect().centerx
# textRect.centery = windowSurface.get_rect().centery

# # making the background white
# windowSurface.fill(white)

# # draw a polygon onto the surface
# pygame.draw.polygon(windowSurface, green, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
