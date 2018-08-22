import tensorflow as tf
import pandas as pd
import numpy as np
import math
from Batches import BatchList
from Vocabulary import Vocabulary


class Model:

    def __init__(self, embedding_size=50, epochs=10, learning_rate=0.01, optimizer="SGD", model_file=None):
        self.checkConstructorParameters(embedding_size, epochs, learning_rate, optimizer)
        self.dataframe = None
        self.vocabulary = None
        self.context_batch = None
        self.batch_size = None
        self.embedding_size = embedding_size
        self.vocabulary_size = None
        self.epochs = epochs
        self.learning_rate = learning_rate
        self.optimizer = optimizer.lower()
        self.model_file = model_file

    def set_input(self, preprocessed_data, input):
        self.vocabulary = preprocessed_data[0]
        self.context_batch = preprocessed_data[1]
        self.texts = preprocessed_data[2]
        self.batch_size = self.context_batch.batch_size
        self.vocabulary_size = self.vocabulary.getVocabSize()
        self.dataframe = input

    def addPlaceholders(self):
        self.train_dataset = tf.placeholder(tf.int32, shape=[self.batch_size])
        self.train_labels = tf.placeholder(tf.int32, shape=[self.batch_size, self.vocabulary_size])

    def addSoftmaxVariables(self):
        self.embeddings = tf.Variable(
            tf.random_uniform([self.vocabulary_size, self.embedding_size], -1.0, 1.0))
        self.hidden_weights = tf.Variable(
            tf.truncated_normal([self.embedding_size, self.vocabulary_size],
                                stddev=1.0 / math.sqrt(self.embedding_size)))
        self.hidden_biases = tf.Variable(tf.zeros([self.batch_size, self.vocabulary_size]))

    def addEmbeddingLookup(self):
        self.embedded_batch = tf.nn.embedding_lookup(self.embeddings, self.train_dataset)

    def addHiddenLayer(self):
        self.logits = tf.add(tf.matmul(self.embedded_batch, self.hidden_weights), self.hidden_biases)

    def addSoftmaxCrossEntropyLoss(self):
        self.loss = tf.reduce_mean(
            tf.nn.softmax_cross_entropy_with_logits_v2(
                labels=self.train_labels, logits=self.logits),
            axis=0)

    def addSGDOptimizer(self):
        self.optimizer = tf.train.GradientDescentOptimizer(self.learning_rate).minimize(self.loss)

    def addAdamOptimizer(self):
        self.optimizer = tf.train.AdamOptimizer().minimize(self.loss)

    def addAdagradOptimizer(self):
        self.optimizer = tf.train.AdagradOptimizer(self.learning_rate).minimize(self.loss)

    def createDataFrameOutput(self):
        vector_column = []
        embedding_lookup_table = self.embeddings.eval()
        for text in self.texts:
            word_tokens = text.tokens
            vector_tokens = np.zeros([self.embedding_size])
            for word in word_tokens:
                word_index = Vocabulary.getIndex(word)
                if word_index is not None:
                    vector_tokens += embedding_lookup_table[word_index, :]
            vector_column.append(vector_tokens)
        pd_column = pd.DataFrame({'VECTOR': vector_column})
        self.dataframe['VECTOR'] = pd_column['VECTOR']
        return self.dataframe

    def computeCosineSimilarity(self):
        pass
        # norm = tf.sqrt(tf.reduce_sum(tf.square(self.mbeddings), 1, keepdims=True))
        # normalized_embeddings = self.embeddings / norm
        # valid_embeddings = tf.nn.embedding_lookup(normalized_embeddings, self.valid_dataset)
        # self.similarity = tf.matmul(valid_embeddings, tf.transpose(normalized_embeddings))        

    def addSaver(self):
        self.model_file = tf.train.Saver()

    def fit(self):
        self.addPlaceholders()
        self.addSoftmaxVariables()
        self.addEmbeddingLookup()
        self.addHiddenLayer()
        self.addSoftmaxCrossEntropyLoss()

        if self.optimizer == "sgd":
            self.addSGDOptimizer()
        elif self.optimizer == "adam":
            self.addAdamOptimizer()
        elif self.optimizer == "adagrad":
            self.addAdagradOptimizer()

        if self.model_file:
            self.addSaver()

        init = tf.global_variables_initializer()
        with tf.Session() as sess:
            sess.run(init)
            total_loss = 0
            iteration = 1
            for _ in range(self.epochs):
                next_batch = self.context_batch.next()
                while next_batch is not None:
                    _, loss_value = sess.run([self.optimizer, self.loss], feed_dict={self.train_dataset: next_batch[0],
                                                                                     self.train_labels: next_batch[1]})
                    total_loss += loss_value
                    mean_loss = total_loss / iteration
                    iteration += 1
                    print("iteration:", iteration)
                    print("mean loss:", mean_loss)
                    next_batch = self.context_batch.next()
                print("----------------------------------------")
                print(self.embeddings.eval())
            return self.createDataFrameOutput()

    def checkConstructorParameters(self, embedding_size, epochs, learning_rate, optimizer):
        if embedding_size < 1:
            raise ValueError("embedding size should be greater than 0")
        if epochs < 1:
            raise ValueError("epoch value should be greater than 0")
        if optimizer.lower() != ("sgd" or "adam" or "adagrad"):
            raise ValueError("wrong optimizer selected")

    def check_input_parameters(self, preprocessed_data, input):
        if len(preprocessed_data) != 3:
            raise ValueError("invalid preprocessed data")
        if pd.DataFrame.__instancecheck__(input) is False:
            raise ValueError("not a dataframe object")
