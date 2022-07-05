# importing everything from the tkinter module
from tkinter import *

# Create a window for the application 
root = Tk()

# Create labels for starters (Just defining the objects)
myLabel1 = Label(root, text="Assalamualaikum, Dunya!")
myLabel2 = Label(root, text="My name is Dhuulfiqaar ibn Junaid!")

# Placing and positioning the objects in the window
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)

# Event loop constantly looping to listen for each loop (even the moving mouse)
root.mainloop()