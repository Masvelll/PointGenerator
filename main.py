import pygame
from pointer import Pointer
from configs import map, size, screen

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
            
    screen.blit(map, (0, 0))
    ptr.update()
    pygame.display.flip()

    clock.tick(60)

pygame.quit()