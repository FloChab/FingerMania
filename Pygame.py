import pygame
import time
from Tiles import Tiles
from Arrow import Arrow
from Label import Label
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 920))
clock = pygame.time.Clock()
running = True
dt = 0

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


# Création les images de label
mauvais = Label("mauvais.png")
ok = Label("ok.png")
bien = Label("bien.png")
tb = Label("tb.png")
parfait = Label("parfait.png")
labels =[mauvais, ok, bien, tb,parfait]


# Couleurs
black = (0, 0, 0)
white = (255, 255, 255)

# Position et taille de la flèche
arrow_x_fixe = screen.get_width() // 2 - 2*arrow_size[0]
arrow_y_fixe = 100
arrow_y_pop = 400

jeu = Tiles(1,2,32)
tiles = jeu.get_tiles()
tiles_delay = jeu.get_tiles_delay()
k = None
arrows=[]
img_arrows=[arrow_left, arrow_down, arrow_up,arrow_right]
for i in range(len(tiles)):
    for j in range(len(tiles[i])):
        if tiles[i][j] == 1:
            arrows.append(Arrow(arrow_x_fixe+j*arrow_size[0],img_arrows[j],tiles_delay[i],j))
timer = time.time()
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(jeu.score)
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # Afficher l'image de la flèche
    screen.blit(arrow_left_fixe, (arrow_x_fixe, arrow_y_fixe))
    screen.blit(arrow_down_fixe, (arrow_x_fixe+1*arrow_size[0], arrow_y_fixe))
    screen.blit(arrow_up_fixe, (arrow_x_fixe+2*arrow_size[0], arrow_y_fixe))
    screen.blit(arrow_right_fixe, (arrow_x_fixe+3*arrow_size[0], arrow_y_fixe))

    #Affiche une fleche qui monte
    #print(time.time()-timer)
    for arrow in arrows:
        if arrow.get_delay() <= time.time()-timer:
            screen.blit(arrow.img,(arrow.x,arrow.y))
            arrow.move()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        for arrow in arrows:
            if arrow.direction == 0:
                if(arrow.is_y_valid()==True):
                    points = 100 - abs(arrow.y - arrow_y_fixe)
                    jeu.add_score(points)
                    k = jeu.wich_label(points)
                    screen.blit(labels[k].image, (labels[k].x,labels[k].y))
                    arrows.remove(arrow)
                    break
    if keys[pygame.K_DOWN]:
        for arrow in arrows:
            if arrow.direction == 1:
                if (arrow.is_y_valid() == True):
                    points = 100 - abs(arrow.y - arrow_y_fixe)
                    jeu.add_score(points)
                    k = jeu.wich_label(points)
                    screen.blit(labels[k].image, (labels[k].x, labels[k].y))
                    arrows.remove(arrow)
                    break

    if keys[pygame.K_UP]:
        for arrow in arrows:
            if arrow.direction == 2:
                if (arrow.is_y_valid() == True):
                    points = 100 - abs(arrow.y - arrow_y_fixe)
                    jeu.add_score(points)
                    k = jeu.wich_label(points)
                    screen.blit(labels[k].image, (labels[k].x, labels[k].y))
                    arrows.remove(arrow)
                    break
    if keys[pygame.K_RIGHT]:
        for arrow in arrows:
            if arrow.direction == 3:
                if (arrow.is_y_valid() == True):
                    points = 100 - abs(arrow.y - arrow_y_fixe)
                    jeu.add_score(points)
                    k = jeu.wich_label(points)
                    screen.blit(labels[k].image, (labels[k].x, labels[k].y))
                    arrows.remove(arrow)
                    break
    if k != None:
        screen.blit(labels[k].image, (labels[k].x, labels[k].y))

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()