import random
import pygame
import os
import time
from Label import Label
from Arrow import *
from Music import Music

FONT_PATH = os.path.join(os.path.dirname(__file__), 'PressStart2P-Regular.ttf')
class Mode:
    def __init__(self):
        self.score = 0
        self.timer = None
        self.nb_tiles = 50
        self.tiles = []
        self.music = Music()
    # self.labels = [Label("mauvais.png"), Label("ok.png"), Label("bien.png"), Label("tb.png"), Label("parfait.png")]
        self.arrows = []
        arrow_left = pygame.image.load("arrow_left.png")
        arrow_down = pygame.image.load("arrow_down.png")
        arrow_up = pygame.image.load("arrow_up.png")
        arrow_right = pygame.image.load("arrow_right.png")
        self.img_arrows = [arrow_left, arrow_down, arrow_up, arrow_right]
    def create_tiles(self):
        for i in range(self.nb_tiles):
            tile = random.choice([0, 1, 2, 3])
            self.tiles.append(tile)

    def wich_label(self, points):
        if points <= 0:
            return 0
        elif points > 0 and points <= 25:
            return 1
        elif points > 25 and points <= 50:
            return 2
        elif points > 50 and points <=75:
            return 3
        elif points > 75 and points < 100:
            return 4
        elif points == 100 :
            return 5

    def init(self):
        pass




class Classic(Mode):
    def __init__(self,screen):
        Mode.__init__(self)
        self.tiles_delay = []
        self.level = None
        self.x_arrow = screen.get_width() // 3
        self.y_arrow_fixe = screen.get_height() // 8
        self.width_arrow = self.x_arrow // 4
        self.y_arrow_pop = screen.get_height() - self.width_arrow
        self.arrow_left_fixe = pygame.transform.scale(pygame.image.load("arrow_left_fixe.png"), (self.width_arrow, self.width_arrow))
        self.arrow_down_fixe = pygame.transform.scale(pygame.image.load("arrow_down_fixe.png"), (self.width_arrow, self.width_arrow))
        self.arrow_up_fixe = pygame.transform.scale(pygame.image.load("arrow_up_fixe.png"),(self.width_arrow, self.width_arrow))
        self.arrow_right_fixe = pygame.transform.scale(pygame.image.load("arrow_right_fixe.png"), (self.width_arrow, self.width_arrow))


    def create_tiles(self):


            # Niveau 1 : combinaisons d'une seule flèche
            if self.level == 1:
                for i in range(self.nb_tiles):
                    # Générer une liste avec 3 zéros et un seul un
                    sequence1 = [0, 0, 0, 1]
                    # Mélanger la liste de manière aléatoire
                    random.shuffle(sequence1)
                    # Ajout de la liste à notre tableau de combinaisons
                    self.tiles.append(sequence1)

            # Niveau 2 : combinaisons d'une ou deux flèches
            elif self.level == 2:
                for i in range(self.nb_tiles):
                    # Générer une liste avec 3 zéros et un seul un
                    sequence1 = [0, 0, 0, 1]
                    # Générer une liste avec 2 zéros et 2 uns
                    sequence2 = [0, 0, 1, 1]
                    # Mélanger les listes de manière aléatoire
                    random.shuffle(sequence1)
                    random.shuffle(sequence2)
                    # Probabilités d'obtenir les séquences
                    probabilities = [0.6, 0.4]
                    # Choix de la séquence à ajouter, au hasard entre les deux
                    sequence = random.choices([sequence1, sequence2], probabilities)
                    # Ajout de la liste à notre tableau de combinaisons
                    self.tiles.append(sequence[0])
            # Niveau 3 : combinaisons d'une, deux ou trois flèches
            elif self.level == 3:
                for i in range(self.nb_tiles):
                    # Générer une liste avec 3 zéros et un seul un
                    sequence1 = [0, 0, 0, 1]
                    # Générer une liste avec 2 zéros et 2 uns
                    sequence2 = [0, 0, 1, 1]
                    # Générer une liste avec 2 zéros et 2 uns
                    sequence3 = [0, 1, 1, 1]
                    # Mélanger les listes de manière aléatoire
                    random.shuffle(sequence1)
                    random.shuffle(sequence2)
                    random.shuffle(sequence3)
                    # Probabilités d'obtenir les séquences
                    probabilities = [0.4, 0.3, 0.3]
                    # Choix de la séquence à ajouter, au hasard entre les trois
                    sequence = random.choices([sequence1, sequence2, sequence3], probabilities)
                    # Ajout de la liste à notre tableau de combinaisons
                    self.tiles.append(sequence[0])

    def create_tiles_delay(self):

        # Niveau 1 : combinaisons d'une seule flèche
        if self.level == 1:
            delai = 0
            for i in range(self.nb_tiles):
                # Ajout du délai
                self.tiles_delay.append((round(2.3 + delai, 1)))
                delai += 2.3

        # Niveau 2 : combinaisons d'une ou deux flèches
        elif self.level == 2:
            delai = 0
            for i in range(self.nb_tiles):
                # Ajout du délai
                self.tiles_delay.append((round(2.0 + delai, 1)))
                delai += 2.0

        # Niveau 3 : combinaisons d'une, deux ou trois flèches
        elif self.level == 3:
            delai = 0
            for i in range(self.nb_tiles):
                # Ajout du délai
                self.tiles_delay.append((round(1.7 + delai, 1)))
                delai += 1.7

    def create_arrows(self):
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                if self.tiles[i][j] == 1:
                    self.arrows.append(Arrow_with_time(self.x_arrow + j * self.width_arrow, self.y_arrow_pop, pygame.transform.scale(self.img_arrows[j],(self.width_arrow, self.width_arrow)), j, self.tiles_delay[i]))

    def init(self):
        self.create_tiles()
        self.create_tiles_delay()
        self.create_arrows()
        self.timer = time.time()
    def display_score(self, screen, x, y, w, h, text_color=(0, 0, 0), border_color=(0, 0, 0), background_color=(255, 255, 255)):

        font_size = h // 6
        font = pygame.font.Font(FONT_PATH, font_size)
        text_font = font.render("Score: {}".format(self.score), True, text_color)
        rect_score = text_font.get_rect(center=(w // 2, h // 2))
        surface_score = pygame.Surface((w, h))
        surface_score.fill(background_color)  # Remplir le rectangle avec la couleur blanc
        pygame.draw.rect(surface_score, border_color, surface_score.get_rect(), 4)  # Dessiner le contour noir
        surface_score.blit(text_font, rect_score)
        screen.blit(surface_score, (x, y))
    def play(self,screen):
        screen.fill("purple")
        # Afficher les images de flèches fixe
        screen.blit(self.arrow_left_fixe, (self.x_arrow, self.y_arrow_fixe))
        screen.blit(self.arrow_down_fixe, (self.x_arrow + 1 * self.width_arrow, self.y_arrow_fixe))
        screen.blit(self.arrow_up_fixe, (self.x_arrow + 2 * self.width_arrow, self.y_arrow_fixe))
        screen.blit(self.arrow_right_fixe, (self.x_arrow + 3 * self.width_arrow, self.y_arrow_fixe))
        # Afficher le score
        self.display_score(screen, self.x_arrow // 4, screen.get_height() // 8, 2*self.width_arrow, self.width_arrow)

        for arrow in self.arrows:
            if arrow.get_delay() <= time.time() - self.timer:
                screen.blit(arrow.img, (arrow.x, arrow.y))
                arrow.move()
            if arrow.y < 0:
                self.arrows.remove(arrow)

    def arrow_pressed(self, direction):
        for arrow in self.arrows:
            if arrow.direction == direction:
                if arrow.is_y_valid(self.y_arrow_fixe,self.width_arrow):
                    points = round(100 - abs(arrow.y - self.y_arrow_fixe)/self.width_arrow*100)
                    self.score += points
                    k = self.wich_label(points)
                    self.arrows.remove(arrow)
                    return k
        points = -50
        self.score += points
        k = self.wich_label(points)
        return k

class Multi_Arrows(Mode):
    def __init__(self, screen):
        Mode.__init__(self)
        self.tiles_delay = []
        self.level = None
        self.width_arrow = screen.get_width() // 6
        self.x_arrow = screen.get_width() // 2 - self.width_arrow // 2
        self.y_arrow_fixe = self.width_arrow
        self.y_arrow_pop = screen.get_height() - self.width_arrow # Bas de l'écran
        self.arrow_multi_fixe = pygame.transform.scale(pygame.image.load("multi_arrow_fixe.png"),
                                                      (self.width_arrow, self.width_arrow))
    def create_tiles_delay(self):
        delai = 0
        for i in range(self.nb_tiles):
            # Ajout du délai
            self.tiles_delay.append((round(2.0+delai, 1)))
            delai += 2

    def create_arrows(self):
        for i in range(len(self.tiles)):
            self.arrows.append(Arrow_with_time(self.x_arrow, self.y_arrow_pop,
                                                       pygame.transform.scale(self.img_arrows[self.tiles[i]], (self.width_arrow, self.width_arrow)), self.tiles[i], self.tiles_delay[i]))

    def init(self):
        self.create_tiles()
        self.create_tiles_delay()
        self.create_arrows()
        self.timer = time.time()

    def display_score(self, screen, x, y, w, h, text_color=(0, 0, 0), border_color=(0, 0, 0), background_color=(255, 255, 255)):

        font_size = h // 6
        font = pygame.font.Font(FONT_PATH, font_size)
        text_font = font.render("Score: {}".format(self.score), True, text_color)
        rect_score = text_font.get_rect(center=(w // 2, h // 2))
        surface_score = pygame.Surface((w, h))
        surface_score.fill(background_color)  # Remplir le rectangle avec la couleur blanc
        pygame.draw.rect(surface_score, border_color, surface_score.get_rect(), 4)  # Dessiner le contour noir
        surface_score.blit(text_font, rect_score)
        screen.blit(surface_score, (x, y))

    def arrow_pressed(self, direction):
        for arrow in self.arrows:
            if arrow.direction == direction:
                if arrow.is_y_valid(self.y_arrow_fixe, self.width_arrow):
                    points = round(100 - abs(arrow.y - self.y_arrow_fixe)/self.width_arrow*100)
                    self.score += points
                    k = self.wich_label(points)
                    self.arrows.remove(arrow)
                    return k
        points = -50
        self.score += points
        k = self.wich_label(points)
        return k

    def play(self,screen):
        screen.fill("purple")
        # Afficher les images de flèches fixe
        screen.blit(self.arrow_multi_fixe, (self.x_arrow, self.y_arrow_fixe))
        # Afficher le score
        self.display_score(screen, screen.get_width() // 6, screen.get_height() // 8, screen.get_width() // 6, self.width_arrow)

        for arrow in self.arrows:
            if arrow.get_delay() <= time.time() - self.timer:
                screen.blit(arrow.img, (arrow.x, arrow.y))
                arrow.move()
            if arrow.y < 0:
                self.arrows.remove(arrow)

class Chrono(Mode):
    def __init__(self):
        Mode.__init__(self)