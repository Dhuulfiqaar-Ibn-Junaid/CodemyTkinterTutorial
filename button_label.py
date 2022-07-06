# importing everything from the tkinter module
from tkinter import *

# Create a window for the application 
root = Tk()

# Define a function to be executed if my_btn clicked
def myClick():
    my_lbl = Label(root, text="Look! I clicked a Button!")
    my_lbl.pack()

# Create a button widget
my_btn = Button(root, text="Click Me", padx=50, pady=50, command=myClick)
"""
1) padx and pady for the spacing inside the button 
2) state=DISABLED to forbid clicking a button
3) just add the command to the attribute of the button and it should work just like in javascript
4) We don't need to add the parentheses after the function name in the command attribute of the function
5) Change the text color of the button using fg (foreground) and the button using bg (background)
"""

# Just simply pack the button without worrying about the position on the window
my_btn.pack()

# Event loop constantly looping to listen for each loop (even the moving mouse)
root.mainloop()