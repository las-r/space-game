import math
import pygame

# initialization and setup
pygame.init()
font = pygame.font.Font()

# settings
WINWIDTH, WINHEIGHT = 800, 600

# main variables
curposx, curposy = 0, 0

# rocket object
class Rocket():
    # initialize
    def __init__(self):
        # position
        self.posx = WINWIDTH // 10
        self.posy = WINHEIGHT // 2

        # values
        self.speed = 1

    # set position
    def setPos(self, x, y):
        self.posx = x
        self.posy = y

    # move from position
    def move(self, x, y):
        self.posx += x
        self.posy += y

# setup display
pygame.display.set_mode((WINWIDTH, WINHEIGHT))
pygame.display.set_caption("space game")

# main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
