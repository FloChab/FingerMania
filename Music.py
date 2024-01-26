import pygame
import time

class Music:
    def __init__(self, chemin):
        self.chemin = chemin

    def play_music(self):
        # Initialisation de la musique
        pygame.mixer.init()
        pygame.mixer.music.load(self.chemin)
        # Lancer la musique
        pygame.mixer.music.play()
        # Attendre 2 secondes pour que la musique puisse être entendue
        time.sleep(2)

    def stop_music(self):
        # Arrêter la musique à la fin de la partie
        pygame.mixer.music.stop()
