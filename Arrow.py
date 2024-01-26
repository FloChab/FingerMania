import pygame

class Arrow():

    def __init__(self, x, img, delay,direction):
        self.direction = direction
        self.img = img
        self.delay = delay
        self.x = x
        # Coordonnée y
        self.y = 600

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_delay(self):
        return self.delay

    def move(self):

        self.y-=5

    def is_y_valid(self):
        if self.y > 0 and self.y < 200:
            return True
        else:
            return False



