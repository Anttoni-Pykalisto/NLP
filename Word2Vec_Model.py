import tensorflow as tf
import math

class Model:
    
    def __init__(self, batch_size = 0, embedding_size = 0, vocabulary_size = 0):
        self.batch_size = batch_size
        self.embedding_size = embedding_size
        self.vocabulary_size = vocabulary_size

    def addEmbeddingSize(self, size):
        self.embedding_size = size

    def addVocabularySize(self, size):
        self.vocabulary_size = size

    def createPlaceholders(self):
        self.train_dataset = tf.placeholder(tf.int32, shape=[self.batch_size])
        self.train_labels = tf.placeholder(tf.int32, shape=[self.batch_size, self.vocabulary_size])
        #self.valid_dataset = tf.constant(valid_examples, dtype=tf.int32)

    def createSoftmaxVariables(self):
        self.embeddings = tf.Variable(
            tf.random_uniform([self.vocabulary_size, self.embedding_size], -1.0, 1.0))
        self.hidden_weights = tf.Variable(
            tf.truncated_normal([self.embedding_size, self.vocabulary_size], stddev = 1.0 / math.sqrt(self.embedding_size)))
        self.hidden_biases = tf.Variable(tf.zeros([self.batch_size, self.vocabulary_size]))

    def embeddingLookup(self):
        print(self.embeddings.shape)
        self.embedded_batch = tf.nn.embedding_lookup(self.embeddings, self.train_dataset)
        print(self.embedded_batch.shape)

    def creatingHiddenLayer(self):
        self.logits = tf.add(tf.matmul(self.embedded_batch, self.hidden_weights), self.hidden_biases)

    def computeSoftmaxCrossEntropyLoss(self):
        self.loss = tf.reduce_mean(
            tf.nn.softmax_cross_entropy_with_logits_v2(
                labels=self.train_labels, logits=self.logits), 
                axis = 0)
    
    def computeCrossEntropyLoss(self):
        # self.loss = tf.reduce_mean(
        #     tf.nn.softmax_cross_entropy_with_logits(labels = , logits = ), axis = 0)
        pass

    def createSGDOptimizer(self):
        self.optimizer = tf.train.GradientDescentOptimizer(1.0).minimize(self.loss)

    def computeCosineSimilarity(self):
        pass
        # norm = tf.sqrt(tf.reduce_sum(tf.square(self.mbeddings), 1, keepdims=True))
        # normalized_embeddings = self.embeddings / norm
        # valid_embeddings = tf.nn.embedding_lookup(normalized_embeddings, self.valid_dataset)
        # self.similarity = tf.matmul(valid_embeddings, tf.transpose(normalized_embeddings))

    def createInitializerVariable(self):
        self.init = tf.global_variables_initializer()

    def createSaver(self):
        self.saver = tf.train.Saver()

    def startTraining(self, batch):
        self.createPlaceholders()
        print("placeholders created")
        print(self.train_dataset)
        print(self.train_labels)
        self.createSoftmaxVariables()
        print("softmax variables created")
        self.embeddingLookup()
        print("embedding lookup created")
        self.creatingHiddenLayer()
        print("hiddenlayer created")
        self.computeSoftmaxCrossEntropyLoss()
        print("softmax loss computed")
        self.createSGDOptimizer()
        print("optimizer created")
        self.createInitializerVariable()
        print("created initiliazer variables")
        with tf.Session() as sess:
            sess.run(self.init)
            average_loss = 0
            next_batch = batch.next()
            while next_batch is not None:
                _, loss_value = sess.run([self.optimizer, self.loss], feed_dict = {self.train_dataset : next_batch[0], self.train_labels : next_batch[1]})
                average_loss += loss_value
                print(average_loss)
                next_batch = batch.next()

# loss = tf.nn.softmax_cross_entropy_with_logits(labels = y, logits = x)
# mean_loss = tf.reduce_mean(loss, axis = 0)
# with tf.Session() as sess:
#     value = sess.run(mean_loss)
#     print(value)

# #######

# hidden_layer = tf.add(tf.matmul(x, weights_hidden), biases_hidden)
# optimizer = tf.train....