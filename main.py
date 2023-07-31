import pygame
from pointer import Pointer
from configs import map, size, screen
from opener import open_map

pygame.init()
pygame.display.set_caption("RandomPointGenerator")

done = False
clock = pygame.time.Clock()
ptr = Pointer()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONUP:
            ptr.change_pos()
        if event.type == pygame.KEYDOWN:
            x, y = ptr.get_coords()
            open_map(x, y)
            
            
    screen.blit(map, (0, 0))
    ptr.update()
    pygame.display.flip()

    clock.tick(60)

pygame.quit()