import pygame
import random

pygame.init()  # initializes Pygame
pygame.display.set_caption("random walk")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
clock = pygame.time.Clock()
xpos = 400  # start point for x
ypos = 400  # start point for y
xdir = 10
ydir = 10


playerImage = pygame.image.load("1.png")
playerImage = pygame.transform.scale(playerImage, (150, 150))

while True:
    map = [
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    ]

    brick = pygame.image.load("brick.png")
    brick2 = pygame.image.load("brick2.png")

    # render section---------------------------------------------

    dir = [1, 2, 3, 4]

    # Render section---------------------------------------------

    for i in range(10000):
        direction = random.choice(dir)

        if direction == 1:
            if ypos - ydir >= 0 and map[(ypos - ydir) // 40][xpos // 40] == 2:
                ypos -= ydir
        elif direction == 2:
            if xpos + xdir < 800 and map[ypos // 40][(xpos + xdir) // 40] == 2:
                xpos += xdir
        elif direction == 3:
            if ypos + ydir < 800 and map[(ypos + ydir) // 40][xpos // 40] == 2:
                ypos += ydir
        elif direction == 4:
            if xpos - xdir >= 0 and map[ypos // 40][(xpos - xdir) // 40] == 2:
                xpos -= xdir

        map[ypos // 40][xpos // 40] = 0

        moves = [
            (xpos, ypos - ydir),
            (xpos + xdir, ypos),
            (xpos, ypos + ydir),
            (xpos - xdir, ypos),
        ]

        canmove = any(map[y // 40][x // 40] == 2 for x, y in moves)

        if not canmove:
            break

        # Start back in the middle if you go off the screen
        if xpos > 800 or xpos < 0:
            xpos = 400
        if ypos > 800 or ypos < 0:
            ypos = 400

        screen.fill((0, 0, 0))

        for i in range(20):
            for j in range(20):
                if map[i][j] == 2:
                    screen.blit(brick, (j * 40, i * 40), (0, 0, 40, 40))
                else:
                    screen.blit(brick2, (j * 40, i * 40), (0, 0, 40, 40))

        screen.blit(playerImage, (xpos, ypos))

        pygame.display.flip()

        clock.tick(60)

pygame.quit()