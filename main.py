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

# Our container lists that will
# populate with our buttons, duels
# and the appropriate windows.

duels = [Duel()] * 6
duel_windows = [None] * 6
buttons = [None] * 6

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

def handleRing(index):
    if duels[index].ring == "Default":
       createRing(index)

    elif duels[index].ring != "Default":
        showWindow(duel_windows[index])

    else:
        index += 1
        createRing(index)

def hideWindow(window):
    window.withdraw()

def showWindow(window):
    window.deiconify()

def createRing(index):
    # duel_windows[index] = Toplevel()
    # duels[index].setRingName(input("Select a ring name: "))
    # duel_windows[index].title(duels[index].ring)
    # hideButton = tk.Button(duel_windows[index], height=2, width=10, text="Hide Me", command=partial(hideWindow, duel_windows[index])).grid()
    # buttons[index].configure(text=duels[index].ring)

    duels[index].gameLoop()

    duel_windows[index].mainloop()

# Instantiating ring buttons

i = 0
while i < 6:
    buttons[i] = tk.Button(main_frame, height=2, width=10, text="Create Ring", command=partial(handleRing, 0))
    i += 1

# Adding the ring buttons to the grid
# within the main frame.

buttons[0].grid(row=0, column=0)
buttons[1].grid(row=0, column=1)
buttons[2].grid(row=1, column=0)
buttons[3].grid(row=1, column=1)
buttons[4].grid(row=2, column=0)
buttons[5].grid(row=2, column=1)



root.mainloop()