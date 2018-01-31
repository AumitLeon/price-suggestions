## Kaggle Mercai Price Suggestion Challenge! 

This project focuses on the price suggestion challenge posted by Mercari on Kaggle: https://www.kaggle.com/c/mercari-price-suggestion-challenge


Contributers: Aumit Leon, Mariana Echeverria

### Getting Started
Download the dataset from https://www.kaggle.com/c/mercari-price-suggestion-challenge/data (train.tsv.7z)

#### Decompressing the Data (MAC): 
Update brew
```
brew update
```

Instal p7zip (tool to work with 7z compression)
```
brew install p7zip
```

Extract! 
```
7z x train.tsv.7z
```

To open the file as a CSV within Excel, run the following the command using the `convert.py` script provided. (`train.tsv`) should be in the same directory as the convert script, and the csv file will also be created in the same script. 

```
python convert.py < train.tsv > train.csv
```
### Feature Extraction
We are planning on using a bag-of-words approach to this problem. We will be matrix where every row corresponds to a training example. 

We preprocessed data by removing punctiation, making all terms lowercase, removing stop words, and adding the name of items as descriptions for items that had no descriptions.

We created a function `createMatrix` that will create a matrix where every row corresponds to a single training example. 
* The first 5000 column positions correspond to the 5000 most frequent words. The vector will have a 1 in the position corresponding to a particular word if that word is present in that item's description, 0 otherwise. 
* The next 1288 columns correspond to the categories represented in the training set. An item gets a 1 in the position corresponding to a particular category if that is the category for that particualr item -- 0 for all other 1287 entries. 
* The next 5 columns are representative of the condition of the item. A 1 in the position that represents the item's condition, 0 every where else. 
* The last column corresponds to shipping-- a 1 if it ships, 0 otherwise.

Thus, the dimensions of the feature/training example matrix will be 1482535x6294 