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
from featureExtraction import readFile, cleanDescriptions, preProcess, getMostFrequentWords, countCategories, createMatrix, test
invalidChars = set(string.punctuation)

def create_model():
    # BOILERPLATE CODE FOR MODEL. NEED TO CREATE A MORE EFFECTIVE MODEL
    # NOTE: MODEL DIMENSIONS ARE CURRENTLY WRONG. NEED TO COVERT AND CATEGORIZE OUTPUTS. 
    model = Sequential()

    # Our examples of 90 features, so input_dim = 90
    model.add(Dense(units=100, activation='relu', input_dim=90))
    model.add(Dense(units=100, activation='relu', kernel_regularizer=regularizers.l2(0.00001)))
    model.add(Dense(units=100, activation='relu', kernel_regularizer=regularizers.l2(0.00001)))
    model.add(Dense(units=100, activation='relu', kernel_regularizer=regularizers.l2(0.00001)))
    model.add(Dense(units=100, activation='relu'))
    #model.add(Flatten())


if __name__ == "__main__":
    filename = "/mnt/c/Users/Aumit/Documents/GitHub/kaggle-mercari/train.csv"
    df, item_des, item_name, cat_name, brand_name, shipping, item_conds  = readFile(filename)
    fin_list = preProcess(item_des, item_name, df, item_name, brand_name)
    #print brand_name

    #countCategories(cat_name)

    freq_words = getMostFrequentWords(fin_list)
    
    examples = createMatrix(freq_words, cat_name, shipping, item_conds, brand_name, fin_list)

    # Create keras model here

    print "Size of matrix " + str(len(examples))

   


    
