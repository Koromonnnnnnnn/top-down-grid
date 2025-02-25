import pygame
import random
import math


# from last year hyperspeed
class ParticleSystem:
    def __init__(self, surface):
        self.surface = surface
        self.xpos = []
        self.ypos = []
        self.xVel = []
        self.yVel = []
        self.sizes = []
        self.colors = []
        self.speed = 6
        self.angle = 0
        self.hue = 0

    def hue_to_rgb(self, hue):
        h = hue / 60.0
        c = 255
        x = c * (1 - abs((h % 2) - 1))
        r = g = b = 0

        if 0 <= h < 1:
            r, g, b = c, x, 0
        elif 1 <= h < 2:
            r, g, b = x, c, 0
        elif 2 <= h < 3:
            r, g, b = 0, c, x
        elif 3 <= h < 4:
            r, g, b = 0, x, c
        elif 4 <= h < 5:
            r, g, b = x, 0, c
        elif 5 <= h < 6:
            r, g, b = c, 0, x

        return (int(r), int(g), int(b))

    def update_particles(self):
        self.angle += 1
        if self.angle > 360:
            self.angle = 0

        radians = math.radians(self.angle)

        for i in range(1):
            if len(self.xpos) < 1000:
                velX = random.uniform(-1, 1)
                velY = random.uniform(-1, 1)
                magnitude = math.sqrt(velX**2 + velY**2)
                if magnitude != 0:
                    normalizedVelX = self.speed * velX / magnitude
                    normalizedVelY = self.speed * velY / magnitude
                else:
                    normalizedVelX = 0
                    normalizedVelY = 0

                self.xpos.append(640)
                self.ypos.append(360)
                self.sizes.append(1)
                self.colors.append(self.hue_to_rgb(self.hue))
                self.xVel.append(normalizedVelX)
                self.yVel.append(normalizedVelY)

        for i in range(len(self.xpos)):
            self.xpos[i] += self.xVel[i]
            self.ypos[i] += self.yVel[i]
            self.sizes[i] += 0.03

            if (
                self.xpos[i] < 0
                or self.xpos[i] > 1280
                or self.ypos[i] < 0
                or self.ypos[i] > 720
            ):
                self.xpos[i] = 640
                self.ypos[i] = 360
                self.sizes[i] = 1
                velX = random.uniform(-1, 1)
                velY = random.uniform(-1, 1)
                magnitude = math.sqrt(velX**2 + velY**2)
                if magnitude != 0:
                    self.xVel[i] = self.speed * velX / magnitude
                    self.yVel[i] = self.speed * velY / magnitude
                else:
                    self.xVel[i] = 0
                    self.yVel[i] = 0

                self.colors[i] = self.hue_to_rgb(self.hue)

        self.hue += 1
        if self.hue >= 360:
            self.hue = 0

    def draw_particles(self):
        for i in range(len(self.xpos)):
            pygame.draw.circle(
                self.surface,
                self.colors[i],
                (int(self.xpos[i]), int(self.ypos[i])),
                int(self.sizes[i]),
            )