class Batches:
	def __init__(self, contexts, batch_size):
		self.batch_number=0
		self.batch_size=batch_size
		self.batches=self.create_batches(contexts)
		self.batch=self.get_batch(self.batches,self.batch_number)


	def create_batches(self,contexts):
		total=[]
		for sentence in contexts:
			for pairings in sentence:
				total.append(pairings)
		return total

	def get_batch(self,batches,batch_number):
		self.batch_number=batch_number
		return batches[batch_number*self.batch_size:(batch_number+1)*self.batch_size]


	def next(self):
		self.batch_number+=1
		if self.batch_number>len(self.batches)/self.batch_size:
			self.batch_number=0
			return self.get_batch(self.batches,self.batch_number)
		else:
			return self.get_batch(self.batches,self.batch_number)
		


#test=[[['help','me'],['those','are']],[['why','me']],[['what','is']],[['help','me']]]
#batch=Batches(test,2)
#print(batch.batch)
#print(batch.next())
#print(batch.next())
#print(batch.next())