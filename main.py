import sys

class Node(): 
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

# TODO create StackFrontier for DFS uses nodes to create it.  
class StackFrontier():
    def __init__(self):
        self.frontier = []
    # adds node to frontier
    def add(self, node):
        return
    #checks if state is in frontier
    def contains_state(self, state):
        return
    #checks if frontier is empty
    def empty(self):
        return len(self.frontier) == 0
    #Removes a node
    def remove(self):
        return
# TODO creat QueueFrontier for BFS
class QueueFrontier(StackFrontier):
    #same as before except for remove
    def remove(self):
# TODO write algorithm 
# Define nodes, stores state, parent node, action taken to get from parent node to here, path cost from initial state
# define frontier, where we can go.
# needs to have an explored set
# first check if frontier is empty, if so, problem is unsolvable
# remove a node from frontier
# does the removed node contain the goal state?  if so we have found the solution
# if not Expand the node (find all the new nodes that could be reached from this node), and add resulting nodes to the frontier. Add the current node to the explored set.
