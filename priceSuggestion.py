# Price Suggestion

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import string
import keras
from keras.models import Sequential 
from keras.layers import Dense
from keras.layers import Flatten
from sklearn import preprocessing
from keras import regularizers
from keras.utils import np_utils, generic_utils
from featureExtraction import readFile, cleanDescriptions, preProcess, getMostFrequentWords, countCategories, createMatrix
invalidChars = set(string.punctuation)

def create_model():
    # BOILERPLATE CODE FOR MODEL. NEED TO CREATE A MORE EFFECTIVE MODEL
    # NOTE: MODEL DIMENSIONS ARE CURRENTLY WRONG. NEED TO COVERT AND CATEGORIZE OUTPUTS. 
    model = Sequential()

    # Our examples of 90 features, so input_dim = 90
    model.add(Dense(units=100, activation='relu', input_dim=1513))
    model.add(Dense(units=100, activation='relu', kernel_regularizer=regularizers.l2(0.00001)))
    model.add(Dense(units=100, activation='relu', kernel_regularizer=regularizers.l2(0.00001)))
    model.add(Dense(units=100, activation='relu', kernel_regularizer=regularizers.l2(0.00001)))
    model.add(Dense(units=100, activation='relu'))

    # Tune the optimizer
    #sgd = optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy',
                optimizer='sgd',
                metrics=['accuracy'])

    return model
        #model.add(Flatten())


if __name__ == "__main__":
    # Local
    #filename = "/mnt/c/Users/Aumit/Documents/GitHub/kaggle-mercari/train.csv"
    #Server
    filename = "../small_train.csv"
    df, item_des, item_name, cat_name, brand_name, shipping, item_conds, prices  = readFile(filename)

    fin_list = preProcess(item_des, item_name, df, item_name, brand_name)
    #print brand_name

    #countCategories(cat_name)

    freq_words = getMostFrequentWords(fin_list)
    
    examples = createMatrix(freq_words, cat_name, shipping, item_conds, brand_name, fin_list)

    # Create keras model here

    print ("Size of matrix " + str(len(examples)))

    # Verify the size of the vectors
    print ("Size of vector 1: " +  str(len(examples[0])))
    print ("Size of vector 2: " + str(len(examples[1])))  


    # NOTE: NEEDS TESTING **********************************************************************************8

    # Initialize Model
    price_model = create_model()
    
    # Training/Test Split
    training_examples_raw = examples[:4500]
    test_examples_raw = examples[4600:4900]

    # Convert to NP arrays: 
    training_examples = np.array(training_examples_raw)
    test_examples = np.array(test_examples_raw)

    prices = list(map(int, prices))
    training_labels_raw = prices[:4500]
    test_labels_raw = prices[4600:4900]

    # Convert labels to nparray
    training_labels = np.array(training_labels_raw)
    test_labels = np.array(test_labels_raw)


    # Convert to categorical in order to produce proper output
    y_train = keras.utils.to_categorical(training_labels, num_classes=2009)

    y_test = keras.utils.to_categorical(test_labels, num_classes=2009)

    # Train the model!
    model.fit(training_examples, y_train, epochs=100, batch_size=15)

    print ("Creating Plots!")
    print (history_1.history.keys())

    #accuracy
    plt.figure(1)
    plt.plot(history_1.history['acc'])
    plt.plot(history_1.history['val_acc'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')

    plt.savefig("model_acc.png")

    #loss
    plt.figure(2)
    plt.plot(history_1.history['loss'])
    plt.plot(history_1.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')

    plt.savefig("model_loss.png")



    

    
   


    
