import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

size = (1600, 800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

done = False
clock = pygame.time.Clock()

map = pygame.image.load("map.png").convert()
map = pygame.transform.scale(map, size)

while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)
    screen.blit(map, (0, 0))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()