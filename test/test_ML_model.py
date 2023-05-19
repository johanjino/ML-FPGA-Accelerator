import tensorflow as tf
from matplotlib import pyplot as plt
import numpy as np



def create_model():

    # linear equation x + y = 10
    data, data_ref = [], []
    for i in range(500):
        for i in range(50):
            data.append(np.array([5+i,5-i]))
            data.append(np.array([5-i,5+i]))
            data_ref.extend([1,1])
            record = np.random.randint(np.random.randint(1,50), size=2)
            if record.sum() != 10: 
                data.append(record)
                data_ref.append(0)
    for i in range(1000):
        record = np.random.randint(np.random.randint(1,50), size=2)
        if record.sum() != 10: 
            data.append(record)
            data_ref.append(0)

    # Define the neural network model
    model = tf.keras.Sequential([
        tf.keras.layers.InputLayer(input_shape=(2,)),  # Input layer with 3 neurons
        tf.keras.layers.Dense(units=4, activation='relu'),  # Hidden layer with 8 neurons and ReLU activation
        tf.keras.layers.Dense(units=1, activation='sigmoid')  # Output layer with 1 neuron and sigmoid activation
    ])

    # Compile the model with binary crossentropy loss and Adam optimizer
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Train the model on some example data
    history = model.fit(tf.convert_to_tensor(data), tf.convert_to_tensor(data_ref), validation_split = 0.3, epochs=5, batch_size=4)
    print(history.history.keys())
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['loss'])
    #plt.plot(history.history['val_accuracy'])
    #plt.plot(history.history['val_loss'])
    plt.title('model accuracy')
    plt.ylabel('accuracy/loss')
    plt.xlabel('datasize (%)')
    plt.legend(['accuracy', 'loss'], loc='upper left')
    plt.show()
    model.save("test_ML.h5")

def model_load():
    model = tf.keras.models.load_model('test/test_ML.h5')
    return model

#create_model()

model = model_load()
print(model.predict([[10,2]]))
print(model.predict([[-2,7]]))
print(model.predict([[5,5]]))