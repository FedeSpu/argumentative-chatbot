import pandas as pan
import os.path


class ReadDataSet:

    def __init__(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        os.chdir(dir_path)
        file = "../DataSet/Evidence.csv"
        self.matrix = pan.read_csv(file)

    def get_matrix(self):
        return self.matrix
