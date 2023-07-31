import pygame
import random
from configs import pointer, size, screen

pygame.init()

class Pointer():
    """Класс указателя рандомного положения"""
    def __init__(self):
        self.image = pointer
        x = random.randrange(0, size[0])
        y = random.randrange(0, size[1])
        self.pos = (x, y)
    
    def update(self):
        screen.blit(self.image, self.pos)
        print(f"Drawed, position -> {self.pos}")