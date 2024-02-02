import random

import pygame
import time

class Music:

    def __init__(self):
        music1 = "Music/m1.mp3"
        music2 = "Music/m2.mp3"
        music3 = "Music/m3.mp3"
        music4 = "Music/m4.mp3"
        music5 = "Music/m5.mp3"
        self.music = random.choice([music1, music2, music3, music4, music5])

    def play_music(self):
        # Initialisation de la musique
        pygame.mixer.init()
        pygame.mixer.music.load(self.music)
        # Lancer la musique
        pygame.mixer.music.play()
        # Attendre 1 secondes pour que la musique puisse être entendue
        time.sleep(1)

    def stop_music(self):
        # Arrêter la musique à la fin de la partie
        pygame.mixer.music.stop()


