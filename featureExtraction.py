# AFeature Extraction for Mercari Price Suggestion Competition 
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import string
invalidChars = set(string.punctuation)

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

    return df, item_description, item_name, category_name, brand_name, shipping

"Currently removes unnecessary punctuation"
def preProcess(item_descript, df):

    df['rev'] = df['item_description'].astype(str)
    temp_descript = df['rev'].tolist()
    final_list = []

    # For every item description
    for i in range(len(temp_descript)):

        # Split by space
        temp_helper = temp_descript[i].split()
        for u in range(len(temp_helper)):

            # If the last char in a word is punctuation
            if temp_helper[u][-1:] in invalidChars:
               word = temp_helper[u][:-1]
               temp_helper[u] = word       
            else:
                continue

        final_list.append(temp_helper)

    return final_list




if __name__ == "__main__":
    filename = "/mnt/c/Users/Aumit/Documents/GitHub/kaggle-mercari/train.csv"
    df, item_des, item_name, cat_name, brand_name, shipping  = readFile(filename)
    fin_list = preProcess(item_des, df)

    # Verify that puncuation was properly removed.
    for y in range(10):
        print fin_list[y]

