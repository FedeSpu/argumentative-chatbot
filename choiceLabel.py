from tkinter import *


def create(root):
    baseLab = Label(root)
    l = Label(baseLab, text="Which answer you like?")
    l.grid(row=0, column=0)
    b = Button(baseLab, text='First')
    b.grid(row=0, column=1)
    b2 = Button(baseLab, text='Second')
    b2.grid(row=0, column=2)
    b3 = Button(baseLab, text='Third')
    b3.grid(row=0, column=3)
    return baseLab
