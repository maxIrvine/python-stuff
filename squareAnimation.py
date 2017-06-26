import pygame
 
pygame.init()
width=1000
height=1000
 
screen = pygame.display.set_mode( ( width, height) )
redSquare = pygame.image.load("/Users/mirvine/DigitalCrafts-06-2017/python/square-512.png").convert()
fpsClock = pygame.time.Clock()
imageX= 200; # x coordnate of image
imageY= 30; # y coordinate of image
running = True
black = ( 0 , 0 , 0)
while (running): # main game loop
    imageX -= 20 
    screen.fill(black) # clear screen 
    screen.blit(redSquare , (imageX, imageY) ) # paint to screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            x, y = event.pos
    pygame.display.update()
    fpsClock.tick(30)
#loop over, quite pygame
pygame.quit()