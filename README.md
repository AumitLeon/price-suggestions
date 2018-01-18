## Kaggle Mercai Price Suggestion Challenge! 

This project depends on the Mercari dataset available at: https://labrosa.ee.columbia.edu/millionsong/


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

