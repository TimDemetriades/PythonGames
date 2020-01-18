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
playerX_change = 0.0

def player(x,y):
    screen.blit(playerImg, (x, y))   # blit is for drawing

# Game Loop
# Prevents screen from closing until you quit
running = True  # make false to close screen
while running:

    # RGB - Red, Green, Blue 
    screen.fill((255, 0, 0))      # 0,0,0 = black

    for event in pygame.event.get():    #checks if event occured
        if event.type == pygame.QUIT:
            running = False

    # if key is pressed, check if it was right or left
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -0.15
        if event.key == pygame.K_RIGHT:
            playerX_change = 0.15
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0.0

    playerX = playerX + playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 800 - 64:   # screen width - player width
        playerX = 736

    player(playerX,playerY)    #must draw player after drawing screen so it appears on top
    pygame.display.update()     # update screen