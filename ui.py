from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Pathing visualizer")
mainframe = ttk.Frame(root) #add padding if needed
mainframe.grid(column=80, row=80)

for i in range(0,80):
    for j in range(0, 80):
        b = Button(, text=str(i), command=partial(btn_click, i)