import numpy as np
    
def relu(array):
    return np.maximum(0,array)
    
def sigmoid(array):
    return 1/(1 + np.exp(-array))