import pygame
from pygame.locals import *
from KT_Button import *
import sys

# Define constants
GRAY = (200, 200, 200)
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 100
FRAMES_PER_SECOND = 30 

# 2 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

oButton = KT_Button(window, (170, 30), "images/button_up.png", "images/button_down.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if oButton.button_update(event):
            print("Someone pressed the button.")


    window.fill(GRAY)
    oButton.draw()
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)   





