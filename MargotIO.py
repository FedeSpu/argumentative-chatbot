import subprocess as sub
from pathlib import Path
import os
from tkinter import *


class MargotIO:

    def __init__(self):
        self.base = Tk()
        self.base.title('Margot Input')
        self.base.geometry("500x300")
        self.base.resizable(width=FALSE, height=FALSE)
        self.inputTxt = Text(self.base, height=15, bg="white")
        sendBtn = Button(self.base, text="Confirm", command=self._calculate)
        # scrollbar = Scrollbar(base, command=inputTxt.yview, cursor="heart")
        # inputTxt['yscrollcommand'] = scrollbar.set
        self.inputTxt.pack()
        sendBtn.pack()
        self.hide()

    def hide(self):
        self.base.withdraw()

    def show(self):
        self.base.deiconify()

    def _calculate(self):
        input_user = self.inputTxt.get(1.0, END)
        if len(input_user) > 0:
            # Save the current working directory for restoring it after running margot
            python_cwd = os.getcwd()
            # home = str(Path.home())
            # Change current working directory with the margot one, otherwise it doesn't work
            os.chdir("../predictor")

            # Sample.txt will be replaced by the user's input
            input_file = 'input.txt'
            f = open(input_file, 'w+')
            f.write(input_user)
            f.close()
            output_dir = 'output/'

            print("Start")
            p = sub.Popen(['bash', 'run_margot.sh', input_file, output_dir])
            # Wait until bash program has finished
            p.communicate()
            print("Finish")
            self.dispose()

    def dispose(self):
        self.base.destroy()
