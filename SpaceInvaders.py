# Space Invaders

import pygame
import random
import math

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
enemyImg = []       #empty list
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 5

for i in range (num_of_enemies):
    enemyImg.append(pygame.image.load("mike.png")) 
    enemyX.append(random.randint(0,735))      # spawns between 0 and 800 on x-axis
    enemyY.append(random.randint(50,150))     # spawns between 50 and 150 on y-axis
    enemyX_change.append(1.5)
    enemyY_change.append(30)

# Bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0      
bulletY = 480
bulletX_change = 0
bulletY_change = 7.5
bullet_state = "ready"
# Ready = you can't see the bullet
# Fire = the bullet is moving

# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)     # font style and size

textX = 10  # score x coordinate
textY = 10  # score y coordinate

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))

def player(x, y):
    screen.blit(playerImg, (x, y))   # blit is for drawing

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))   # blit is for drawing

def fire_bullet(x, y):
    global bullet_state             # let's us change this variable
    bullet_state = "fire"
    screen.blit(bulletImg,(x + 16, y + 10)) # +16 and +10 so it fires from the top center of the ship

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))   #distance formula
    if distance < 27:
        return True
    else:
        return False

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

    # if key is pressed, check if it was right or left or space
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -3
        if event.key == pygame.K_RIGHT:
            playerX_change = 3
        if event.key == pygame.K_SPACE:
            if bullet_state is "ready":     # check if bullet is being fired
                bulletX = playerX           # sets bullet to shoot from where ship is
                fire_bullet(bulletX, bulletY)

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
    for i in range(num_of_enemies):
        enemyX[i] = enemyX[i] + enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 1.5
            enemyY[i] = enemyY[i] + enemyY_change[i]
        elif enemyX[i] >= 800 - 64:   # screen width - player width
            enemyX_change[i] = -1.5
            enemyY[i] = enemyY[i] + enemyY_change[i]
        
        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)   # stores true or false
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value = score_value + 1
            # then respawn enemy
            enemyX[i] = random.randint(0,735)      # spawns between 0 and 800 on x-axis
            enemyY[i] = random.randint(50,150)     # spawns between 50 and 150 on y-axis

        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement
    if bulletY <= 0:            # when bullet passes top of screen
        bulletY = 480           # move it back to the ship
        bullet_state = "ready"  # and change state back to ready

    if bullet_state is "fire":              # when bullet is fired
        fire_bullet(bulletX, bulletY)       # draw bullet
        bulletY = bulletY - bulletY_change  # move bullet in y direction

    player(playerX,playerY)    #must draw player after drawing screen so it appears on top
    show_score(textX,textY)

    pygame.display.update()     # update screen