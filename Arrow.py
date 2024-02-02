import pygame

class Arrow:

    def __init__(self, x, y, img, direction):
        self.direction = direction
        self.img = img
        self.x = x
        self.y = y

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def move(self):
        self.y-=5

    def is_y_valid(self, y_fixe, width_arrow):
        if self.y > y_fixe - width_arrow  and self.y < y_fixe + width_arrow:
            return True
        else:
            return False

class Arrow_with_time(Arrow):
    def __init__(self, x, y, img, direction, delay):
        Arrow.__init__(self, x, y, img, direction)
        self.delay = delay
    def get_delay(self):
        return self.delay

