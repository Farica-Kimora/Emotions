import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Emotional Computer")

# Load sprites
happy_sprite = pygame.image.load("happy_sprite.png")
sad_sprite = pygame.image.load("sad_sprite.png")

# Initial mood
current_mood = "happy"

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update mood randomly every 3 seconds
    if pygame.time.get_ticks() % 3000 == 0:
        current_mood = random.choice(["happy", "sad"])

    # Display mood
    screen.fill((255, 255, 255))  # White background

    if current_mood == "happy":
        screen.blit(happy_sprite, (width // 2 - 50, height // 2 - 50))
    elif current_mood == "sad":
        screen.blit(sad_sprite, (width // 2 - 50, height // 2 - 50))

    pygame.display.flip()

    clock.tick(60)  # Cap the frame rate to 60 frames per second

# Quit Pygame
pygame.quit()