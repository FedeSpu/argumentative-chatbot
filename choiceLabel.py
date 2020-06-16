from tkinter import *
import renforcement as ref


def create(root, ev_res, ev_user):
    baseLab = Label(root)
    l = Label(baseLab, text="Which answer you like?")
    l.grid(row=0, column=0)
    b = Button(baseLab, text='None', command=lambda: baseLab.destroy())
    b.grid(row=0, column=1)
    for i in range(len(ev_res)):
        b = Button(baseLab, text=str(i+1), command=lambda: vote(ev_res[i], ev_user, baseLab))
        b.grid(row=0, column=i+2)
    return baseLab


def vote(ev_res, ev_user, baseLab):
    ref.increase(ev_user, ev_res[2])
    baseLab.destroy()
