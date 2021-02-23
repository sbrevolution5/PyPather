import pygame
import math

WIDTH = 800
#initialize window
WINDOW = pygame.display.set_mode((WIDTH,WIDTH))#always square
pygame.display.set_caption("Path finding")
#Color constants-------
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)
ORANGE = (255,155,0)
TEAL = (64,244,208)
#Classes --------
class Spot:
    def __init__(self, row, col, width, height):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = row * height
        self.color = WHITE
        self.width = width
        self.height = height
        self.neighbors = []
    # determine position
    def get_pos(self):
        return (self.col, self.row)

    #