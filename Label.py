import pygame

class Label():
    def __init__(self,chemin):
        self.x = 100
        self.y = 400
        self.label_size = (200, 200)
        self.image = pygame.transform.scale(pygame.image.load(chemin), self.label_size)

