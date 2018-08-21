from Finding import Finding
from Vocabulary import Vocabulary
from Context import Context
from Batches import BatchList
from os import listdir
from os.path import isfile, join
import numpy as np
import pandas as pd
from pandas import *
import csv
import os



class Preprocessing:
	def __init__(self, input=None,vocabulary_input=None, vocabulary_min_frequency=3, vocabulary_max_size=300,remove_stopwords="on",stemming="on",create_context="on",context_window_size=2,create_batches="on",batch_size=30):
		self.vocabulary_input=vocabulary_input
		self.vocabulary_min_frequency=vocabulary_min_frequency
		self.vocabulary_max_size=vocabulary_max_size
		self.remove_stopwords=remove_stopwords
		self.stemming=stemming
		self.create_context=create_context
		self.context_window_size=context_window_size
		self.create_batches=create_batches
		self.batch_size=batch_size
		self.input=input

	def set_input(self,input):
		self.input=input
	
	def preprocess(self):
		index=self.input['ID'].tolist()
		finding_text=self.input['TEXT'].tolist()
		all_finding=[]
		all_text=[]
		if self.vocabulary_input==None:
			vocabulary = Vocabulary(self.vocabulary_min_frequency,self.vocabulary_max_size)
		else:
			vocabulary=self.vocabulary_input

		for i in range(len(index))
			finding = Finding(index[i], text[i],self.remove_stopwords,self.stemming)
			vocabulary.appendSet(finding.tokens)
			all_finding.append(finding)
			all_text += finding.sentences
		vocabulary.buildDataSets()
		if self.create_context=="on":
			context = Context(all_text, self.context_window_size)
		if self.create_context=="on" and self.create_batches=="on":
			batch = BatchList(context.context, self.batch_size, len(vocabulary.word_list))
		return [vocabulary,batch,all_finding]
