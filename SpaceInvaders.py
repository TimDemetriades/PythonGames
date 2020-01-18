# Space Invaders

import pygame
import random

# Initialize the pygame
pygame.init()

# Create the screen , width = 800 and height = 600
screen = pygame.display.set_mode((800,600)) 

# Background
background = pygame.image.load("background1.png")

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("spaceship.png")   
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0.0

# Enemy
enemyImg = pygame.image.load("mike.png")
enemyX = random.randint(0,800)      # spawns between 0 and 800 on x-axis
enemyY = random.randint(50,150)     # spawns between 50 and 150 on y-axis
enemyX_change = 2
enemyY_change = 40

def player(x,y):
    screen.blit(playerImg, (x, y))   # blit is for drawing

def enemy(x,y):
    screen.blit(enemyImg, (x, y))   # blit is for drawing


# Game Loop
# Prevents screen from closing until you quit
running = True  # make false to close screen
while running:

    # RGB - Red, Green, Blue 
    screen.fill((0, 0, 0))      # 0,0,0 = black
    # Background Image
    screen.blit(background,(0,0))

    for event in pygame.event.get():    #checks if event occured
        if event.type == pygame.QUIT:
            running = False

    # if key is pressed, check if it was right or left
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -3
        if event.key == pygame.K_RIGHT:
            playerX_change = 3
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0.0

    #Player movement
    playerX = playerX + playerX_change

    # Boundary checking
    if playerX <= 0:
        playerX = 0
    elif playerX >= 800 - 64:   # screen width - player width
        playerX = 736

    # Enemy movement
    enemyX = enemyX + enemyX_change
    if enemyX <= 0:
        enemyX_change = 2
        enemyY = enemyY + enemyY_change
    elif enemyX >= 800 - 64:   # screen width - player width
        enemyX_change = -2
        enemyY = enemyY + enemyY_change

    player(playerX,playerY)    #must draw player after drawing screen so it appears on top
    enemy(enemyX, enemyY)
    pygame.display.update()     # update screen