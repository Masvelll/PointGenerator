import pygame

RED = (255, 0, 0)
size = (1760, 800)

pygame.init()
screen = pygame.display.set_mode(size)

map = pygame.image.load("map.png").convert()
map = pygame.transform.scale(map, size)

pointer = pygame.image.load("pointer.png").convert()
pointer = pygame.transform.scale(pointer, (90, 50))
pointer.set_colorkey((0, 0, 0))