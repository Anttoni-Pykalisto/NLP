from Finding import Finding
from Vocabulary import Vocabulary
from Context import Context
from Batches import BatchList
from os import listdir
from os.path import isfile, join
import numpy as np
import csv
import os

training_files = ['TrainingText/' + f for f in listdir('TrainingText/') if isfile(join('TrainingText/', f))]

class Preprocessing:
	@staticmethod
	def run(training_files,vocabulary_input=None,remove_stopwords="on",stemming="off",create_context="on",create_batches="on",batch_size=30):
		all_finding = []
		all_text = []
		text = ''
		if vocabulary_input==None:
			vocabulary = Vocabulary(min_frequency = 3, max_size = 300)
		else:
			vocabulary=vocabulary_input
		index = 0
		for f in training_files:
			with open(f, "r", encoding="utf-8") as f:
				line = f.readline()
				text += line
				finding = Finding(index, text,remove_stopwords,stemming)
				vocabulary.appendSet(finding.tokens)
				all_finding.append(finding)
				all_text += finding.sentences
				index += 1
				output=all_text
		if create_context=="on":
			context = Context(all_text, 2)
			output=context
		if create_context=="on" and create_batches=="on":
			batch = BatchList(context.context, batch_size, len(vocabulary.word_list))
			output=batch
		return output

output=Preprocessing.run(training_files)