#Import
import pygame
import time
import sys
import os
from Tiles import Menu
from Arrow import Arrow
from Label import Label
from Mode import *

# pygame setup
pygame.init()
# Initialisation de la fenêtre en mode plein écran
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((1280, 720))
width_screen, height_screen = pygame.display.get_surface().get_size()
pygame.display.set_caption("Menu Pygame")

clock = pygame.time.Clock()
running = True
dt = 0
#pygame.key.set_repeat()


def afficher_texte(message, couleur, y, taille=36, x=None, police=None):
    if police is None:
        police = police_grande
    texte = police.render(message, True, couleur)
    if x is None:
        x = width_screen // 2
    texte_rect = texte.get_rect(center=(x, y))
    screen.blit(texte, texte_rect)
    return texte_rect

def afficher_texte_petit(message, couleur, y, x=None):
    texte = police_petite.render(message, True, couleur)
    if x is None:
        x = width_screen // 2
    texte_rect = texte.get_rect(center=(x, y))
    screen.blit(texte, texte_rect)
    return texte_rect


# Charger la police "Press Start 2P"
FONT_PATH = os.path.join(os.path.dirname(__file__), 'PressStart2P-Regular.ttf')
police_grande = pygame.font.Font(FONT_PATH, 36)
police_petite = pygame.font.Font(FONT_PATH, 18)

# Définir la taille du rectangle
# SCORE_RECT_WIDTH = 200
# SCORE_RECT_HEIGHT = 50

# Création des labels
rate = Label("rate.png",screen)
mauvais = Label("mauvais.png",screen)
ok = Label("ok.png",screen)
bien = Label("bien.png",screen)
tb = Label("tb.png",screen)
parfait = Label("parfait.png",screen)
labels = [rate, mauvais, ok, bien, tb, parfait]

allow_left = True
allow_down = True
allow_up = True
allow_right = True

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (169, 169, 169)
PURPLE = "purple"

jeu = None
keys=None
k = None
arrows=[]
menu = Menu()

while running:
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # Affichage de la bannière "Menu"
    pygame.draw.rect(screen, BLACK, (0, 0, width_screen, 100))
    afficher_texte("Menu", WHITE, 50)

    # Affichage de "FingerMania"
    afficher_texte("FingerMania", WHITE, 200, taille=100)

    # Affichage des boutons
    bouton_y_positions = [300, 400, 500]

    keys = pygame.key.get_pressed()
    if(menu.mode == None):
        for i, y in enumerate(bouton_y_positions):
            pygame.draw.rect(screen, WHITE, (50, y, (width_screen - 100), 80))
            pygame.draw.rect(screen, BLACK, (50, y, (width_screen - 100), 80), 3)
            afficher_texte("Mode {}".format(i + 1), PURPLE, y + 30)

            # Affichage des caractéristiques
            caract = ""
            if i == 0:
                caract = "Classique"
            elif i == 1:
                caract = "Multiflèche"
            elif i == 2:
                caract = "Contre la Montre"
            afficher_texte_petit(caract, PURPLE, y + 60)
    elif(menu.level == None):
        for i, y in enumerate(bouton_y_positions):
            pygame.draw.rect(screen, WHITE, (50, y, (width_screen - 100), 80))
            pygame.draw.rect(screen, BLACK, (50, y, (width_screen - 100), 80), 3)
            afficher_texte("Niveau {}".format(i + 1), PURPLE, y + 30)

            # Affichage des caractéristiques
            caract = ""
            if i == 0:
                caract = "Niveau 1"
            elif i == 1:
                caract = "Niveau 2"
            elif i == 2:
                caract = "Niveau 3"
            afficher_texte_petit(caract, PURPLE, y + 60)
    else:
        if jeu.timer == None:
            print("Initialisation d'une partie")
            jeu.init()
            # print(jeu.arrows)
        if len(jeu.arrows) != 0:
            jeu.play(screen)

            # print(keys)
            if keys[pygame.K_LEFT] and allow_left == True:
                allow_left = False
                k = jeu.arrow_pressed(0)
            if not keys[pygame.K_LEFT]:
                allow_left = True

            if keys[pygame.K_DOWN] and allow_down == True:
                allow_down = False
                k = jeu.arrow_pressed(1)
            if not keys[pygame.K_DOWN]:
                allow_down = True

            if keys[pygame.K_UP] and allow_up == True:
                allow_up = False
                k = jeu.arrow_pressed(2)
            if not keys[pygame.K_UP]:
                allow_up = True

            if keys[pygame.K_RIGHT] and allow_right == True:
                allow_right = False
                k = jeu.arrow_pressed(3)
            if not keys[pygame.K_RIGHT]:
                allow_right = True

            if k is not None:
                screen.blit(labels[k].image, (labels[k].x, labels[k].y))

        else:
            menu.mode = None
            menu.level = None
            jeu.timer = None

    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    # Bouton "Quitter" en bas à droite avec une police spécifique
    rect_quitter = afficher_texte("Quitter", BLACK, height_screen - 30, police=police_petite, x=width_screen - 100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for i, bouton_y in enumerate(bouton_y_positions):
                if 50 <= x <= width_screen - 50 and bouton_y <= y <= bouton_y + 80:#Si on est sur un des boutons
                    if (menu.mode == None):
                        menu.mode = i + 1
                        match i:
                            case 0:
                                jeu = Classic(screen)
                            case 1:
                                jeu = Multi_Arrows()
                            case 2:
                                jeu = Chrono()
                    elif (menu.level == None):
                        jeu.level = i + 1
                        menu.level = i + 1



        # Vérification du clic sur le bouton "Quitter"
    if event.type == pygame.MOUSEBUTTONDOWN and rect_quitter.collidepoint(pygame.mouse.get_pos()):
        pygame.quit()
        sys.exit()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()


