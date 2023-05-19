import numpy as np
import activations

class node:
    def __init__(self, kernel=None, bias=None, activation=None, next=None, name="Unnamed", type="layer") -> None:
        if kernel!=None:
            kernel = np.array(kernel)
        if bias!=None:
            bias = np.array(bias)
        if activation!=None:
            activation = getattr(activations, activation)
        self.kernel = kernel
        self.bias = bias
        self.activation = activation
        self.next = next
        self.name = name
        self.type = type

    def update(self, kernel=None, bias=None, activation=None, next=None, name=None):
        if kernel!=None:
            kernel = np.array(kernel)
            self.kernel = kernel
        if bias!=None:
            bias = np.array(bias)
            self.bias = bias
        if activation!=None:
            activation = getattr(activations, activation)
            self.activation = activation
        if next!=None:
            self.next = next
        if name!=None:
            self.name = name

    def is_empty(self):
        return (self.kernel is None or self.bias is None or self.activation is None)

    def propagate(self, input):
        if self.type == 'head':
            return self.next.propagate(input)
        if self.is_empty():
            raise ValueError("Weights of layer {} {} has not been assigned".format(self.name, self))
        input = np.array(input)
        out = np.matmul(input,self.kernel) + self.bias
        out = self.activation(out)
        if self.next == None:
            return out
        return self.next.propagate(out)
    
