# AFeature Extraction for Mercari Price Suggestion Competition 
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

"""Read CSV and put each column into a list."""
def readFile(filename):
    df = pd.read_csv(filename)     

    # Turn each column into a list
    item_description = df['item_description'].tolist()
    item_name = df['name'].tolist()
    category_name = df['category_name'].tolist()
    brand_name = df['brand_name'].tolist()
    shipping = df['shipping'].tolist()
    #print item_description

    # Verify the lengthts of the lists
    # Each list is of length 1482535! 
    print len(item_description)
    print len(item_name)
    print len(category_name)
    print len(brand_name)
    print len(shipping)


if __name__ == "__main__":
    filename = "/mnt/c/Users/Aumit/Documents/GitHub/kaggle-mercari/train.csv"
    readFile(filename)
