import pygame


class Label():
    def __init__ (self, chemin, screen):
        # Définir la position des labels
        self.x = screen.get_width() // 12
        self.y = screen.get_height() // 2
        self.label_size = (screen.get_width() // 6, screen.get_width() // 6)
        self.image = pygame.transform.scale(pygame.image.load(chemin), self.label_size)
