import pygame
import math

WIDTH = 800
#initialize window
WINDOW = pygame.display.set_mode((WIDTH,WIDTH))#always square
pygame.display.set_caption("Path finding")
#Color constants-------
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)
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
    #color change methods 
    # Boolean accessors is start/is end etc
    # function to fill in neighbors



# create an array (grid) of Spots,
# Draw a grid on screen
def draw_grid(win, rows, width):
# when user clicks mouse on grid, they change the color of the cell
# Allow for a few small buttons to place start and end
# draws background 
def draw(win, grid, rows, width):

# where did the user click?
def get_clicked_pos(pos, rows, width):
#game loop
def main():