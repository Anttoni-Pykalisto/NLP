class Context:
	def __init__(self,sentences, window):
		self.context=self.createContext(sentences,window)

	def createContext(self,sentences,window):
		data=[]
		for sentence in sentences:
			for word_index,word in enumerate(sentence):
				for nb_word in sentence[max(word_index-window,0):min(word_index+window,len(sentence))+1]:
					if nb_word != word:
						data.append([word,nb_word])
		return data