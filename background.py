import pygame


class Background:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("long_road.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 0.75

    def move_direction(self, direction):
        if direction == "up":
            self.y = self.y - self.delta
        if direction == "down":
            self.y = self.y + self.delta

        if self.y > 0:
            self.y = -360
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])