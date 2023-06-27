import numpy as np
    
def relu(array):
    return np.maximum(0,array)
    
def sigmoid(array):
    return 1/(1 + np.exp(-array))

def softmax(array):
    e_array = np.exp(array - np.max(array))
    return e_array / e_array.sum()