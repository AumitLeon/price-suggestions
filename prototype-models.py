import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import string
import keras
from keras.models import Sequential 
from keras.layers import Dense
from keras.layers import Flatten
import numpy as np
from sklearn import preprocessing
from keras import regularizers
from keras.utils import np_utils, generic_utils

""""Begin buildig model..."""