import sys

# Define nodes, stores state, parent node, action taken to get from parent node to here, path cost from initial state
class Node(): 
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

# TODO create StackFrontier for DFS uses nodes to create it.  
# TODO write algorithm 
# define frontier, where we can go.
# needs to have an explored set
# first check if frontier is empty, if so, problem is unsolvable
# remove a node from frontier
# does the removed node contain the goal state?  if so we have found the solution
# if not Expand the node (find all the new nodes that could be reached from this node), and add resulting nodes to the frontier. Add the current node to the explored set.
class StackFrontier():
    def __init__(self):
        self.frontier = []
    # adds node to frontier
    def add(self, node):
        self.frontier.append(node)
    #checks if state is in frontier
    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)
    #checks if frontier is empty
    def empty(self):
        return len(self.frontier) == 0
    #Removes last  node in frontier
    def remove(self):
        if self.empty():
            raise Exception("Empty frontier")
        else:
            node = self.frontier[-1] #last node
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

# TODO create a frontier for greedy best
# todo create frontier for a*


# Maze class which reads from a file,
#Later on this will read from pygame/tkinter
class Maze():
    #initialized
    def __init__(self, filename):

        # Read file and set height and width of maze
        with open(filename) as f:
            contents = f.read()

        # Validate start and goal character A and B respectively
        if contents.count("A") != 1:
            raise Exception("maze must have exactly one start point")
        if contents.count("B") != 1:
            raise Exception("maze must have exactly one goal")

        # Determine height and width of maze
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)
        # Keep track of walls
        self.walls = []
        #create 2d array where False is no wall, True is wall, (A and B turn to false) Has an index error that appends false, each row gets appended to walls array
        for i in range(0, self.height):
            for j in range(0, self.width):
                row = []
                try:
                    if contents[i][j] == "A": 
                        self.start = (i,j)
                        row.append(False)
                    elif contents[i][j]== "B":
                        self.end = (i,j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(True)
            self.walls.append(row)

        #maze has a solution field, starts blank
        self.solution = None

    #prints maze to console returns nothing 
    def print(self):
        #takes self.solution, unless the solution is None,
        solution = self.solution if self.solution is not None else None
        # checks each row/col of walls,
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if(col):
                    print("█", end="")
                elif(i,j) == self.start:
                    print("A", end="")
                elif(i,j) == self.end:
                    print("B", end="")
                elif(i,j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print() #newline
        # prints what belongs there, according to solution
        

    #Function that returns the cells next to whatever the state is. returns an array of all non-wall states(cells)
    def neighbors(self, state):
        row, col = state
        candidates = [
            ("up", (row-1, col))
            ("down", (row+1, col))
            ("left", (row, col-1))
            ("right", (row, col+1))
        ]
        result = []
        #check if the candidates are clear
        for action, (r,c) in candidates:
            #add (action, (row,col)) to result if its valid
    def solve(self):
        #"""Finds a solution to maze, if one exists."""

        # Keep track of number of states explored

        # Initialize frontier to just the starting position

        # Initialize an empty explored set

        # Keep looping until solution found

            # If nothing left in frontier, then no path

            # Choose a node from the frontier

            # If node is the goal, then we have a solution

            # Mark node as explored

            # Add neighbors to frontier
           