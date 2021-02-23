# A simple version of our UI in GUIZero, mainly to use the Waffle widget

# Imports ---------------
from guizero import App, Text, Waffle
#Functions --------
def add_wall():
    

# App -------------------
app = App("Maze")
instructions = Text(app, text="Click the squares to draw a maze them")
board = Waffle(app, width=20, height=20, command=add_wall)
app.display()
