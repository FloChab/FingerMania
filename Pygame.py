#Import
import pygame
import time
import sys
import os
from Tiles import Tiles
from Arrow import Arrow
from Label import Label

# pygame setup
pygame.init()
# Initialisation de la fenêtre en mode plein écran
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((1280, 720))
width_screen, height_screen = pygame.display.get_surface().get_size()
pygame.display.set_caption("Menu Pygame")

clock = pygame.time.Clock()
running = True
dt = 0
pygame.key.set_repeat()

def arrow_pressed(direction):
    for arrow in arrows:
        if arrow.direction == direction:
            if arrow.is_y_valid() == True:
                points = 100 - abs(arrow.y - arrow_y_fixe)
                jeu.add_score(points)
                k = jeu.wich_label(points)
                screen.blit(labels[k].image, (labels[k].x, labels[k].y))
                arrows.remove(arrow)
                return k

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
police_path = os.path.join(os.path.dirname(__file__), 'PressStart2P-Regular.ttf')
police_grande = pygame.font.Font(police_path, 36)
police_petite = pygame.font.Font(police_path, 18)

# Charger les images de fleches
arrow_size = (100, 100)
arrow_left = pygame.transform.scale(pygame.image.load("arrow_left.png"), arrow_size)
arrow_down = pygame.transform.scale(pygame.image.load("arrow_down.png"), arrow_size)
arrow_up = pygame.transform.scale(pygame.image.load("arrow_up.png"), arrow_size)
arrow_right = pygame.transform.scale(pygame.image.load("arrow_right.png"), arrow_size)
arrow_left_fixe = pygame.transform.scale(pygame.image.load("arrow_left_fixe.png"), arrow_size)
arrow_down_fixe = pygame.transform.scale(pygame.image.load("arrow_down_fixe.png"), arrow_size)
arrow_up_fixe = pygame.transform.scale(pygame.image.load("arrow_up_fixe.png"), arrow_size)
arrow_right_fixe = pygame.transform.scale(pygame.image.load("arrow_right_fixe.png"), arrow_size)
img_arrows=[arrow_left, arrow_down, arrow_up,arrow_right]

# Création les images de label
mauvais = Label("mauvais.png")
ok = Label("ok.png")
bien = Label("bien.png")
tb = Label("tb.png")
parfait = Label("parfait.png")
labels = [mauvais, ok, bien, tb, parfait]

allow_left =True
allow_down =True
allow_up =True
allow_right =True

# Couleurs
black = (0, 0, 0)
white = (255, 255, 255)
grey = (169,169,169)
purple = "purple"

# Position et taille de la flèche
arrow_x_fixe = screen.get_width() // 2 - 2*arrow_size[0]
arrow_y_fixe = 100
arrow_y_pop = 400

# Définir la taille du rectangle
largeur_rectangle = 200
hauteur_rectangle = 50

jeu = Tiles()
keys=None
k = None
arrows=[]
timer = None

while running:
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # Affichage de la bannière "Menu"
    pygame.draw.rect(screen, black, (0, 0, width_screen, 100))
    afficher_texte("Menu", white, 50)

    # Affichage de "FingerMania"
    afficher_texte("FingerMania", white, 200, taille=100)

    # Affichage des boutons
    bouton_y_positions = [300, 400, 500]
    if(jeu.mode == None):
        for i, y in enumerate(bouton_y_positions):
            pygame.draw.rect(screen, white, (50, y, (width_screen - 100), 80))
            pygame.draw.rect(screen, black, (50, y, (width_screen - 100), 80), 3)
            afficher_texte("Mode {}".format(i + 1), purple, y + 30)

            # Affichage des caractéristiques
            caract = ""
            if i == 0:
                caract = "Classique"
            elif i == 1:
                caract = "Multiflèche"
            elif i == 2:
                caract = "Contre la Montre"
            afficher_texte_petit(caract, purple, y + 60)
    elif(jeu.niveau == None):
        for i, y in enumerate(bouton_y_positions):
            pygame.draw.rect(screen, white, (50, y, (width_screen - 100), 80))
            pygame.draw.rect(screen, black, (50, y, (width_screen - 100), 80), 3)
            afficher_texte("Niveau {}".format(i + 1), purple, y + 30)

            # Affichage des caractéristiques
            caract = ""
            if i == 0:
                caract = "Niveau 1"
            elif i == 1:
                caract = "Niveau 2"
            elif i == 2:
                caract = "Niveau 3"
            afficher_texte_petit(caract, purple, y + 60)
    else:
        # Efface l'écran
        if timer == None:
            tiles = jeu.get_tiles()
            tiles_delay = jeu.get_tiles_delay()
            for i in range(len(tiles)):
                for j in range(len(tiles[i])):
                    if tiles[i][j] == 1:
                        if jeu.mode == 1 and jeu.niveau !=1:
                            arrows.append(Arrow(arrow_x_fixe + j * arrow_size[0], img_arrows[j], tiles_delay[i], j))
                        else:
                            arrows.append(Arrow(arrow_x_fixe + j * arrow_size[0], img_arrows[j], tiles_delay[i], j))
            timer = time.time()

        if(len(arrows)!=0):
            screen.fill("purple")
            # Afficher l'image de la flèche
            screen.blit(arrow_left_fixe, (arrow_x_fixe, arrow_y_fixe))
            screen.blit(arrow_down_fixe, (arrow_x_fixe + 1 * arrow_size[0], arrow_y_fixe))
            screen.blit(arrow_up_fixe, (arrow_x_fixe + 2 * arrow_size[0], arrow_y_fixe))
            screen.blit(arrow_right_fixe, (arrow_x_fixe + 3 * arrow_size[0], arrow_y_fixe))

            # Afficher le score dans le rectangle violet entouré de gris avec la police "Press Start 2P"
            texte_score = police_petite.render("Score: {}".format(jeu.score), True, black)
            rect_score = texte_score.get_rect(center=(largeur_rectangle // 2, hauteur_rectangle // 2))
            surface_score = pygame.Surface((largeur_rectangle, hauteur_rectangle))
            surface_score.fill(white)  # Remplir le rectangle avec la couleur violet
            pygame.draw.rect(surface_score, black, surface_score.get_rect(), 4)  # Dessiner le contour gris
            surface_score.blit(texte_score, rect_score)

            # Afficher la surface du rectangle sur la fenêtre
            screen.blit(surface_score, (100, 300))

            # Affiche une fleche qui monte
            # print(time.time()-timer)
            for arrow in arrows:
                if arrow.get_delay() <= time.time() - timer:
                    screen.blit(arrow.img, (arrow.x, arrow.y))
                    arrow.move()
                if arrow.y < 0:
                    arrows.remove(arrow)

            keys = pygame.key.get_pressed()

            #print(keys)
            if keys[pygame.K_LEFT] and allow_left == True:
                print("AAAAAA")
                allow_left = False
                k = arrow_pressed(0)
            if keys[pygame.K_LEFT] != True:
                allow_left = True

            if keys[pygame.K_DOWN] and allow_down == True:
                allow_down = False
                k = arrow_pressed(1)
            if keys[pygame.K_DOWN] != True:
                allow_down = True

            if keys[pygame.K_UP] and allow_up == True:
                allow_up = False
                k = arrow_pressed(2)
            if keys[pygame.K_UP] != True:
                allow_up = True

            if keys[pygame.K_RIGHT] and allow_right == True:
                allow_right = False
                k = arrow_pressed(3)
            if keys[pygame.K_RIGHT] != True:
                allow_right = True

            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()

            if k != None:
                screen.blit(labels[k].image, (labels[k].x, labels[k].y))

        else:
            jeu.mode = None
            jeu.niveau = None
            timer = None

    # Bouton "Quitter" en bas à droite avec une police spécifique
    rect_quitter = afficher_texte("Quitter", black, height_screen - 30, police=police_petite, x=width_screen - 100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for i, bouton_y in enumerate(bouton_y_positions):
                if 50 <= x <= width_screen - 50 and bouton_y <= y <= bouton_y + 80:#Si on est sur un des boutons
                    if (jeu.mode == None):
                        jeu.mode = i+1
                    elif (jeu.niveau == None):
                        jeu.niveau = i+1



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


