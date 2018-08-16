from Vocabulary import Vocabulary
import numpy as np

class BatchList:
	def __init__(self, contexts, batch_size):
		self.batch_number = -1
		self.batch_size = batch_size
		self.batch_targets, self.batch_labels = self.create_batches(contexts)
		self.batch_list_size = len(self.batch_targets)

	def create_batches(self,contexts):
		batch_data = []
		label_data = []
		for target, t_context in contexts:
			target_index = Vocabulary.getIndex(target)
			context_index = Vocabulary.getIndex(t_context)
			if target_index is not None and context_index is not None:
				batch_data.append(target_index)
				label_data.append(context_index)
		return batch_data, label_data

	def to_one_hot(self,vocab_size):
		batch_targets=[]
		batch_labels=[]
		for index in self.batch_labels:
			temp = np.zeros(vocab_size)
			temp[index]=1
			batch_labels.append(temp)
		return batch_labels



	def get_batch(self, batch_number):
		self.batch_number = batch_number
		return self.batch_targets[batch_number * self.batch_size : (batch_number+1) * self.batch_size], self.to_one_hot(self.batch_labels[batch_number * self.batch_size : (batch_number+1) * self.batch_size])

	def next(self):
		self.batch_number+=1
		if self.batch_number > (self.batch_list_size / self.batch_size):
			self.batch_number = -1
			return None
		else:
			return self.get_batch(self.batch_number)