import pygame
import random


class Traffic2:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.delta = 2
        self.points_given = False
        self.traffic_list = ["blue_car.png", "gray_van.png", "green_truck.png", "white_cargo_truck.png",
                             "yellow_coupe.png"]
        self.car_rng = random.randint(1, 4)
        self.image = pygame.image.load(self.traffic_list[self.car_rng])
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def move_direction(self, direction):
        if direction == "up":
            self.y = self.y - self.delta
        if direction == "down":
            self.y = self.y + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def traffic_movement(self):
        self.move_direction("down")
        if self.y > 1208:
            self.y = random.randint(-500, -128)
            random_speed = random.randint(-5, 5)
            speed = random_speed / 10
            self.delta = self.delta + speed
            if self.delta < 1:
                self.delta = 1

    def detect_off_screen(self):
        if self.y > 720 and not self.points_given:
            self.points_given = True
            self.car_rng = random.randint(0, 4)
            self.image = pygame.image.load(self.traffic_list[self.car_rng])
            return True
        if 0 < self.y < 720 and self.points_given:
            self.points_given = False
            return False
