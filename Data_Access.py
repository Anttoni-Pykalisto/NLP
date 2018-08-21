from os import listdir
from os.path import isfile, join
import pandas as pd

class TextFileAccess:

    def __init__(self, folder_path):
        training_files = [folder_path + f for f in listdir(folder_path) if isfile(join(folder_path, f))]
        self.id = []
        self.text = []
        self.vector = []
        index = 0
        for f in training_files:
            with open(f, "r", encoding="utf-8") as f:
                self.id.append(index)
                self.text.append(f.readline().replace('\n', ' '))
                index += 1
        
    def retrieve(self):
        return pd.DataFrame({
            'ID' : self.id,
            'TEXT' : self.text,
            'VECTOR' : self.vector})