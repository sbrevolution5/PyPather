# PyPather
An interactive pathfinding visualization written in python with pygame and tkinter

# Instruction
Left click to draw, first placing an orange square as the start, and next a blue square for the end.  Then draw walls for the maze. 
Right click removes walls or entrance/exit.

# Goals
 a. A grid where the user can select two points, and an animated pathfinding algorithm (initially using a*) will find a path in between DONE
 b. allow the user to draw obstacles on the grid, which the algorithm will have to avoid. DONE
 b1. Allow user to import a text file via command line arguments.  A is start B is end, any non whitespace character is a wall.  
 c. allow for different pathfinding algorithms to be used
 d. allow for a "race" between different algorithms. 
