import tkinter as tk
from tkinter import *
from duel import Duel
from functools import partial

# Defining the main application window
# and UI. Main window consists of six
# duel rings that will be visible and
# hidden on toggle.

root = tk.Tk()
root.title("Duel Buddy")
root.geometry("400x400")
root.maxsize(400,400)

root_width = root.winfo_width()
root_height = root.winfo_height()

duels = [Duel()] * 6

# Creating a frame to contain ring buttons. Also
# Centering the ring buttons within the frame.

main_frame = tk.Frame(root, width=root_width, height=root_height)
main_frame.pack()
main_frame.grid_configure(padx=root_width*.2, pady=(root_height//2,0))
main_frame.grid_columnconfigure(weight=1, index=0)

# Handle Ring will first determine if your ring
# is currently in use. If it is not, it will
# provide the template to fill out the ring
# details including: name, duelists and if
# the duel is a title match or not. If it is
# currently a duel in use it will simply display
# the current state of the duel.

def handleRing(integer):
    if duels[integer].ring == "Default":
       createRing(integer)

def hideWindow(window):
    window.withdraw()

def createRing(integer):
    global top
    top = Toplevel()
    top.title("Test")
    hideButton = tk.Button(top, height=2, width=10, text="Hide Me", command=partial(hideWindow, top)).grid()
    top.mainloop()

# Instantiating ring buttons

i = 0
buttons = [None] * 2

while i < 2:
    buttons[i] = tk.Button(main_frame, height=2, width=10, text="Create Ring", command=partial(handleRing, i))
    i += 1

# Adding the ring buttons to the grid
# within the main frame.

buttons[0].grid(row=0, column=0)
buttons[1].grid(row=0, column=1)
# buttons[2].grid(row=1, column=0)
# buttons[3].grid(row=1, column=1)
# buttons[4].grid(row=2, column=0)
# buttons[5].grid(row=2, column=1)



root.mainloop()