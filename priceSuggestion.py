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

if __name__ == "__main__":
    filename = "/mnt/c/Users/Aumit/Documents/GitHub/kaggle-mercari/train.csv"
    df, item_des, item_name, cat_name, brand_name, shipping, item_conds  = readFile(filename)
    fin_list = preProcess(item_des, item_name, df, item_name, brand_name)
    #print brand_name

    #countCategories(cat_name)

    freq_words = getMostFrequentWords(fin_list)
    
    createMatrix(freq_words, cat_name, shipping, item_conds, brand_name, fin_list)

    # Create keras model hereg