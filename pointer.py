import pygame
import random
from configs import pointer, size, screen

pygame.init()

class Pointer():
    """Класс указателя рандомного положения"""
    def __init__(self):
        self.image = pointer
        self.rect = self.image.get_rect()
        x = random.randrange(0, size[0])
        y = random.randrange(0, size[1])
        self.pos = (self.rect.bottom, self.rect.centery)
    
    def update(self):
        screen.blit(self.image, self.pos)
    
    def change_pos(self):
        x = random.randrange(0, size[0])
        y = random.randrange(0, size[1])
        
        self.pos = (x, y)
        
        