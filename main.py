import tkinter as tk
from duel import Duel

# Defining the main application window
# and UI. Main window consists of six
# duel rings that will be visible and
# hidden on toggle.

root = tk.Tk()
root.title("Duel Buddy")
root.geometry("300x300")
root.maxsize(300,300)

root_width = root.winfo_width()
root_height = root.winfo_height()

duels = [Duel()] * 6

# Creating a frame to contain ring buttons. Also
# Centering the ring buttons within the frame.

main_frame = tk.Frame(root, width=root_width, height=root_height)
main_frame.pack()
main_frame.grid_configure(padx=root_width*.2, pady=(root_height//2,0))
main_frame.grid_columnconfigure(weight=1, index=0)

# Command to create a ring containing a duel

def handleRing(index):
    ringName = input("Enter a ring name: ")
    duel = Duel()
    print(duel.ring)
    duel.ring = ringName
    duel.duelist1.setName("Moron")


# Instantiating ring buttons

i = 0
buttons = [None]

while i < 1:
    buttons[i] = tk.Button(main_frame, text="Create Ring", command=handleRing(i))
    i += 1

# Adding the ring buttons to the grid
# within the main frame.

buttons[0].grid(row=0, column=0)
# buttons[1].grid(row=0, column=1)
# buttons[2].grid(row=1, column=0)
# buttons[3].grid(row=1, column=1)
# buttons[4].grid(row=2, column=0)
# buttons[5].grid(row=2, column=1)



root.mainloop()