# Space Invaders

import pygame

# Initialize the pygame
pygame.init()

# Create the screen , width = 800 and height = 600
screen = pygame.display.set_mode((800,600)) 

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("spaceship.png")   
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480

def player():
    screen.blit(playerImg, (playerX,playerY))   # blit is for drawing

# Game Loop
# Prevents screen from closing until you quit
running = True  # make false to close screen
while running:

    # RGB - Red, Green, Blue 
    screen.fill((255, 0, 0))      # 0,0,0 = black

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    player()    #must draw player after drawing screen so it appears on top
    pygame.display.update()     # update screen