from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Coding With Doc")

vertical = Scale(root, from_=0, to=200)
vertical.pack()

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()


root.mainloop()