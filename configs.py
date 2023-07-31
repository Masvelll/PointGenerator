import pygame

RED = (255, 0, 0)
size = (1760, 800)

west = 38.207823
east = 38.428069

north = 54.001234
south = 53.941632

pygame.init()
screen = pygame.display.set_mode(size)

map = pygame.image.load("map.png").convert()
map = pygame.transform.scale(map, size)

pointer = pygame.image.load("pointer.png").convert()
pointer = pygame.transform.scale(pointer, (90, 50))
pointer.set_colorkey((0, 0, 0))