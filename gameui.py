import pygame
import math
import sys
from queue import Queue
from random import randint

MAX_WIDTH = 50 # Maximum number of columns
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
    def __init__(self, row, col, width, height, color=WHITE ):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * height
        self.color = color
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
    #when to call it?
    def update_neighbors(self, grid):
        self.neighbors = []  # erases current neighbors
        # if it isn't the last row and the one below it isn't a wall,
        if self.row < MAX_WIDTH - 1 and not grid[self.row+1][self.col].is_wall():
            # then add that to neighbors
            self.neighbors.append(grid[self.row+1][self.col])
        if self.row > 0 and not grid[self.row][self.col-1].is_wall():
            # then add that to neighbors
            self.neighbors.append(grid[self.row][self.col-1])
        if self.col < MAX_WIDTH - 1 and not grid[self.row][self.col+1].is_wall():
            # then add that to neighbors
            self.neighbors.append(grid[self.row][self.col+1])
        if self.col > 0 and not grid[self.row-1][self.col].is_wall():
            # then add that to neighbors
            self.neighbors.append(grid[self.row-1][self.col])
#Frontier class
class StackFrontier():
    def __init__(self):
        self.frontier = []
        self.explored = []
    # adds node to frontier
    def add(self, node):
        self.frontier.append(node)
    #checks if state is in frontier
    def contains_state(self, state):
        return any(node == state for node in self.frontier)
    #checks if frontier is empty
    def empty(self):
        return len(self.frontier) == 0
    #Removes last  node in frontier
    def explore(self): #previously called remove
        if self.empty():
            print("No solution found")
            return
        else:
            node = self.frontier[-1] #last node
            self.explored.append(node); #adds node to explored set
            self.frontier = self.frontier[:-1] # all except the last one 
            return node
# TODO creat QueueFrontier for BFS
class QueueFrontier(StackFrontier):
    #same as before except for remove
    def remove(self):
        if self.empty():
            raise Exception("Empty frontier")
        else:
            node = self.frontier[0] #first node
            self.frontier = self.frontier[1:] # all except the first one 
            return node
def solve_dfs(grid, start, end,draw):
    #"""Finds a solution to maze, if one exists."""

    # Keep track of number of states explored (LATER FOR A* OR GREEDY BEST)

    # Initialize frontier to just the starting position
    # Initialize an empty explored set
    frontier = StackFrontier()
    frontier.add(start)
    
    # Keep looping until solution found
    while True:
    # If nothing left in frontier, then no path
        if frontier.empty():
            print("Path unfindable")
            return
    # Choose a node from the frontier
        check = frontier.explore()
        # Mark node as explored
    # If node is the goal, then we have a solution
        if end == check:
            print("We Found it!!")
            return
        grid[check.row][check.col].make_closed
    # Add neighbors to frontier unless they have already been explored
        check.update_neighbors(grid)
        for neighbor in check.neighbors:
            grid[neighbor.row][neighbor.col].make_open
            if not frontier.contains_state(neighbor):
                frontier.add(neighbor)
        draw();

# FUNCTIONS ---------------
def rand_maze(path_percent_int = 80):

    # Generates random maze  that is 80% path, Will not always be solvable, but should be----------------
    #Change this to alter percentage of paths
    new_maze = []
    for i in range(0, 50):
        row = []
        for j in range(0,50):
            if randint(1,100) > path_percent_int:
                row.append("C")
            else: 
                row.append(" ")
        new_maze.append(row)
    new_maze[0][0]="A"
    new_maze[48][40]="B"
    return new_maze


# create an array (grid) of Spots,
def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, gap)
            grid[i].append(spot)
    return grid
# switch function for colors
def color_switch(letter):
    switcher = {
        "A": ORANGE,
        "B": TURQUOISE,
        " ": WHITE
    }
    #Anything that is not A B or space is a wall
    return switcher.get(letter, BLACK)
#makes grid from maze array, 
def make_grid_from_maze(rows, width, maze):
    grid = []
    gap = width//rows
    for i in range(0, len(maze)):
        grid.append([])
        for j in range(0, len(maze[i])):
            color = color_switch(maze[i][j])            
            spot = Spot(i,j,gap,gap, color)
            if spot.color == ORANGE:
                start = spot
            elif spot.color == TURQUOISE:
                end = spot
            grid[i].append(spot)
    return grid, start, end
# Draw a grid on screen
def draw_grid(win, rows, width):
    space = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * space), (width, i*space))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j*space, 0), (j*space, width))
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
def turn_red(grid, draw):
    for i in range(0,50):
        for j in range (0,50):
            if grid[i][j].color == BLACK:
                grid[i][j].color = RED
    draw()
# "game" loop
def main(win, width):
    rows = 50
    run = True
    maze = rand_maze()
    gen = True #should the program generate a maze on its own?
    if gen:
        grid, start, end = make_grid_from_maze(rows, width, maze) #makes a random maze 
    else:
        grid = make_grid(rows, width)
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
                if event.key == pygame.K_q:
                    turn_red(grid,lambda:draw(win, grid, rows, width))
                if event.key == pygame.K_SPACE:
                    print("Running pathfinding algorithm, eventually....")
                    solve_dfs(grid, start, end,lambda:draw(win, grid, rows, width))
                if event.key == pygame.K_r:
                    #Creates new random maze
                    maze = rand_maze()
                    start = None
                    end = None
                    grid = make_grid_from_maze(rows, width, maze)
                if event.key == pygame.K_c: # c key will clear board
                    start = None
                    end = None
                    grid = make_grid(rows, width)

    pygame.quit()

main(WINDOW, WIDTH)
