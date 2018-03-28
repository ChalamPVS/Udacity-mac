import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras


# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series, window_size):
    # containers for input/output pairs
    X = []
    y = []
   
    for i in range(len(series)-window_size):
        X.append(series[i:i+window_size])
    y=series[window_size:]
    # reshape each 
    X = np.asarray(X)
 
    y = np.asarray(y)
    y = np.reshape(y, (len(y),1))

    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(window_size):
    model=Sequential()
    model.add(LSTM(5, input_shape=(window_size, 1)))
    model.add(Dense(1, activation='tanh'))
              
    return model         
    


### TODO: return the text input with only ascii lowercase and the punctuation given below included.
def cleaned_text(text):
    punctuation = ['!', ',', '.', ':', ';', '?']
    to_be_removed = ['*', '@']
    
    for r in to_be_removed:
        text=text.replace(r, ' ')
    
    to_be_replaced = {'â':'a', 'à':'a', 'è':'e', 'é':'e'}
    for k,v in to_be_replaced.items():
        text=text.replace(k, v)

    return text

### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text, window_size, step_size):
    # containers for input/output pairs
    inputs = []
    outputs = []
    for i in range(0, len(text)-window_size, step_size):
        inputs.append(text[i:i+window_size])
        outputs.append(text[i+window_size])

    return inputs,outputs

# TODO build the required RNN model: 
# a single LSTM hidden layer with softmax activation, categorical_crossentropy loss 
def build_part2_RNN(window_size, num_chars):
    model=Sequential()
    model.add(LSTM(200, input_shape=(window_size, num_chars)))
    model.add(Dense(num_chars, activation='softmax'))
    
    return model
