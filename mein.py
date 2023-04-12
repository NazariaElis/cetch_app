import pygame

pygame.init()



window_height = 500
window_width = 500
window  = pygame.display.set_mode((window_height,window_width))

def run():
    game = True

    while game:


        for event in pygame.event.get():
