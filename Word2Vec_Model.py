import tensorflow as tf

class Model:
    
    def __init__(self, batch = None, labels = None, embedding_size = None):
        self.batch = batch
        self.labels = labels
        self.embedding_size = embedding_size

    def addBatch(self, batch):
        self.batch = batch

    def addLabels(self, labels):
        self.labels = labels

    def addEmbeddingSize(self, size):
        self.embedding_size = size

    def createPlaceholders(self):
        pass

    def createNCEVariables(self):
        pass 

    def computeNCELoss(self):
        with tf.name_scope('loss'):
            self.loss = tf.reduce_mean(
                tf.nn.nce_loss(
                    weights =
                    biases = 
                    labels = 
                    inputs = 
                    num_sampled =
                    num_classes =
                )
            )

    def createSGDOptimizer(self):
        with tf.name_scope('optimizer'):
            self.optimizer = tf.train.GradientDescentOptimizer(1.0).minimize(loss)

    def computeCosineSimilarity(self):
        pass

    def createInitializerVariable(self):
        self.init = tf.global_variables_initializer()

    def createSaver(self):
        self.saver = tf.train.Saver()

    def startTraining(self):
        pass



# loss = tf.nn.softmax_cross_entropy_with_logits(labels = y, logits = x)
# mean_loss = tf.reduce_mean(loss, axis = 0)
# with tf.Session() as sess:
#     value = sess.run(mean_loss)
#     print(value)

# #######

# hidden_layer = tf.add(tf.matmul(x, weights_hidden), biases_hidden)
# optimizer = tf.train....