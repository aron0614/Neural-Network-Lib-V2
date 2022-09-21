# Copyright 2022 by the author(s) of this code.
# All rights reserved.

#document my code with docstrings and comments as needed to explain what the code is doing and why.
#use the numpy library for all matrix operations



import numpy as np
import math
import random as rand
import json
import logging

#activation functions
def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_prime(x):
    return sigmoid(x)*(1-sigmoid(x))

def tanh(x):
    return np.tanh(x)

def tanh_prime(x):
    return 1.0 - x**2

def relu(x):
    return np.maximum(0,x)

def relu_prime(x):
    return 1*(x>0)

def softmax(x):
    return np.exp(x)/np.sum(np.exp(x), axis=0)

def softmax_prime(x):
    return softmax(x)*(1-softmax(x))


class _Layer:
    def __init__(self, inNodes, outNodes, activation):
        self.inNodes = inNodes
        self.outNodes = outNodes
        self.activation = activation
        self.weights = np.random.randn(inNodes, outNodes)
        self.biases = np.random.randn(outNodes, 1)

    def calculateOutputs(self, inputs):
        weightedInputs = np.zeros((self.outNodes, 1))

        for nodeOutput in range(self.outNodes):
            weightedInput = self.biases[nodeOutput]
            for nodeInput in range(self.inNodes):
                weightedInput += inputs[nodeInput] * self.weights[nodeInput][nodeOutput]
            weightedInputs[nodeOutput] = self.activation(weightedInput)
        
        return weightedInputs

    def nodeCost(self, output, target):
        error = target - output
        return error * error
     

class DataPoint:
    def __init__(self, inputs, targets):
        self.inputs = inputs
        self.targets = targets
    
    def getInput(self, index):
        return self.inputs[index]
    
    def getTarget(self, index):
        return self.targets[index]

    def getInputs(self):
        return self.inputs

    def getTargets(self):
        return self.targets


class NeuralNetwork:
    def __init__(self, layer_sizes : list, learning_rate, activation_function):
        self.layer_sizes = layer_sizes
        self.layers = [] #list of layers
        for i in range(len(layer_sizes)-1):
            self.layers.append(_Layer(layer_sizes[i], layer_sizes[i+1], activation_function)) #create layers
        self.learning_rate = learning_rate
        self.activation_function = activation_function
        
    def calculateOutputs(self, inputs):
        outputs = inputs
        for layer in self.layers:
            outputs = layer.calculateOutputs(outputs)
        return outputs

    def cost(self, dataPoint : DataPoint):
        outputs = self.calculateOutputs(dataPoint.getInputs())
        cost = 0
        for node in range(len(outputs)):
            cost += self.layers[-1].nodeCost(outputs[node], dataPoint.getTarget(node))
        return cost
    
    def avrageCost(self, data : list):
        cost = 0
        for dataPoint in data:
            cost += self.cost(dataPoint)
        return cost/len(data)
    
    def learn(self, data : list, epochs, batch_size):
        for epoch in range(epochs):
            rand.shuffle(data)
            batches = [data[x:x+batch_size] for x in range(0, len(data), batch_size)]
            for batch in batches:
                pass

n = NeuralNetwork([2,3,2], 0.1, sigmoid)
print(n.cost(DataPoint([1,1], [0,1])))
print(n.calculateOutputs([1,2]))
    

