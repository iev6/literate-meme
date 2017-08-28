"""
A small python module implementing MLP using numpy
Supported Activation functions : Sigmoid, ReLU

@author : giridhursriram@gmail.com

Part of PA1, EE6132, Fall 2017
"""
"""
Submission Details
==================
Giridhur S
Roll Number : EE13B129
"""

import numpy as np

class Net:
    def __init__():
        '''
        defines how a new object of class Net is initialized,
        default number of layers = 0,
        '''
        self.layers = [];
        self.layer_dims = [];
        print "Initialized an instance of class Net"

    def add_layer(layer_type="FC",no_neurons=100,activation="Sigmoid"):
        '''
        appends a layer to the existing network,
        default layer type = fully connected (FC) #TODO:
