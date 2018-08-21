from Word2Vec_Model import Model
from Data_Access import TextFileAccess
from Preprocessing import Preprocessing


data = TextFileAccess("TrainingText/")
input = data.retrieve()
preprocess = Preprocessing('''param here''', input)
'''preprocess stuff here'''
vectorization = Model()
vectorization.set_input('''preprocess output''' ,input)
output = vectorization.fit()