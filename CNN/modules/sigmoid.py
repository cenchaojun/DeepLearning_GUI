import tensorflow as tf
from CNN.modules.module import Module



class Sigmoid(Module):
    '''
    Tanh Layer
    '''

    def __init__(self,name='sigmoid'):
        self.name = name
        Module.__init__(self)
        
    def forward(self,input_tensor, batch_size=10, img_dim=28):
        self.input_tensor = input_tensor
        with tf.name_scope(self.name):
            #with tf.name_scope('activations'):
            self.activations = tf.nn.sigmoid(self.input_tensor, name=self.name )
            tf.summary.histogram('activations', self.activations)
        return self.activations

    def clean(self):
        self.activations = None

