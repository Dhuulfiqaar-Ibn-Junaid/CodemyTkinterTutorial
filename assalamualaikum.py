# importing everything from the tkinter module
from tkinter import *

# Create a window for the application 
root = Tk()

# Create a label for starters (Just defining the object)
myLabel = Label(root, text="Assalamualaikum, Dunya!")

# Placing the object defined above into the screen
myLabel.pack()

# Event loop constantly looping to listen for each loop (even the moving mouse)
root.mainloop()