# Space Invaders

import pygame

# Initialize the pygame
pygame.init()

# Create the screen , hieght = 800 and width = 600
screen = pygame.display.set_mode((800,600)) 

# Game Loop
# Prevents screen from closing until you quit
running = True  # make false to close screen
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False