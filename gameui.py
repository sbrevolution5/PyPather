import pygame
import math
from queue import Queue

WIDTH = 800
# initialize window
WINDOW = pygame.display.set_mode((WIDTH, WIDTH))  # always square
pygame.display.set_caption("Path finding")
# Color constants-------
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)
# Classes --------


class Spot:
    def __init__(self, row, col, width, height):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * height
        self.color = WHITE
        self.width = width
        self.height = height
        self.neighbors = []
    # determine position

    def get_pos(self):
        return (self.col, self.row)
    # let me draw the spots

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
    
    # color change methods
    def make_wall(self):
        self.color = BLACK

    def make_start(self):
        self.color = ORANGE

    def make_end(self):
        self.color = TURQUOISE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def reset(self):
        self.color = WHITE

    def make_path(self):
        self.color = PURPLE
    # Boolean accessors is start/is end etc

    def is_wall(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN
    # function to fill in neighbors

    def update_neighbors(self, grid):
        self.neighbors = []  # erases current neighbors
        # if it isn't the last row and the one below it isn't a wall,
        if self.x < self.height-1 and not grid[self.x][self.y+1].is_wall():
            # then add that to neighbors
            self.neighbors.append(grid[self.x][self.y+1])
        if self.x > 0 and not grid[self.x][self.y-1].is_wall():
            # then add that to neighbors
            self.neighbors.append(grid[self.x][self.y-1])
        if self.y < self.width-1 and not grid[self.x+1][self.y].is_wall():
            # then add that to neighbors
            self.neighbors.append(grid[self.x+1][self.y])
        if self.y > 0 and not grid[self.x-1][self.y].is_wall():
            # then add that to neighbors
            self.neighbors.append(grid[self.x-1][self.y])
# create an array (grid) of Spots,


def make_grid(rows, width, height):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, gap)
            grid[i].append(spot)
    return grid



# Draw a grid on screen
def draw_grid(win, rows, width):
    space = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * space), (width, i*space))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j*space, 0), (j*space, width))

# when user clicks mouse on grid, they change the color of the cell
# Allow for a few small buttons to place start and end
# draws background


def draw(win, grid, rows, width):
    win.fill(WHITE)
    for row in grid:
        for spot in row:
            spot.draw(win)
    draw_grid(win, rows, width)
    pygame.display.update()
# where did the user click?


def get_clicked_pos(pos, rows, width):
    y, x = pos;
    gap = width // rows
    row = y // gap
    col = x // gap
    return row, col    
# game loop

def main(win, width):
    
    rows = 50
    run = True
    grid = make_grid(rows, width, width)
    start = None
    end = None
    while(run):
        draw(win, grid, rows, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if pygame.mouse.get_pressed()[0]: #left click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, rows, width)
                spot = grid[row][col]
                if not start and spot != end:
                    start = spot
                    spot.make_start();
                elif not end and spot != start:
                    end = spot
                    spot.make_end();
                else:
                    spot.make_wall()
            if pygame.mouse.get_pressed()[2]: # rclick
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, rows, width)
                spot = grid[row][col]
                spot.reset()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c: # c key will clear board
                    start = None
                    end = None
                    grid = make_grid(rows, width)

    pygame.quit()

main(WINDOW, WIDTH)
