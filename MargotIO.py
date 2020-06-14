# MARGOT IO WINDOW
import subprocess as sub
from pathlib import Path
import os
from tkinter import *
from AnaliseMargotOut import AnaliseMargotOut
import Similarity as sim
import renforcement as renf


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

    # Open margot process, create input.txt file with input of user
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
            self.ev = self.__analise()
            print("Finish")
            self.dispose()

    def dispose(self):
        self.base.destroy()

    # Analise margot output file
    def __analise(self):
        amo = AnaliseMargotOut()
        ev = amo.get_all_evidence()
        cl = amo.get_all_claim()
        cl_ev = amo.get_all_claim_evidence()
        # Return first n (in this case 3) phrases of dataset that match the first evidence
        # Filter with cosine similarity
        filtered = sim.get_n_similarity_ev(ev[0], 10)
        provaLista = [(item[1]) for item in filtered]
        renf.getN(3, provaLista, ev[0])
        return sim.get_n_similarity_ev(ev[0], 3)

    # Return all the evidence of the margot file
    def get_ev(self):
        if hasattr(self, 'ev'):
            return self.ev
        else:
            return None
