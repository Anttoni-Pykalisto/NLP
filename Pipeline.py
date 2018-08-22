from Word2Vec_Model import Model
from Data_Access import TextFileAccess
from Preprocessing import Preprocessing

data = TextFileAccess("TrainingText/")
input = data.retrieve()
preprocessing = Preprocessing()
preprocessing.set_input(input)
(preprocessed_data, original_dataframe) = preprocessing.preprocess()
vectorization = Model()
vectorization.set_input(preprocessed_data, original_dataframe)
output = vectorization.fit()