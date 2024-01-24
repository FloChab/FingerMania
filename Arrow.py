import pygame

class Arrow():

    def __init__(self, x, direction, delay):
        self.direction = direction
        self.delay = delay
        self.x = x
        # Coordonnée y
        self.y = 300

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_delay(self):
        return self.delay

    def moove_arrow(self):

        # Fleche gauche
        if self.direction == 'haut':
            for i in range(self.x):
                y-=





        # Fleche du haut
        elif self.direction == 'droit':


        # Fleche droite
        elif self.direction == 'bas':


        # Fleche du bas
        elif self.direction == 'gauche':


        # Mauvaise direction
        else:
            print("erreur")




