#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 22:32:37 2021

@author: nicole
"""

# Multiple Linear Regression

# Importing the libraries
import pandas as pd
from sklearn.metrics import confusion_matrix

# Importing the dataset
dataset = pd.read_csv('encoding_hashes.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

print(X)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LogisticRegression
classifier_LR = LogisticRegression(random_state = 0)
classifier_LR.fit(X_train, y_train)
# Predicting the Test set results
y_pred_LR = classifier_LR.predict(X_test)


# save the model to disk
import pickle
with open('finalized_LR_model.pkl', 'wb') as file:
    pickle.dump(classifier_LR, file)
    
#import pickle
#filename = 'finalized_LR_model.sav'
#pickle.dump(classifier_LR, open(filename, 'wb'))

## Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_LR = confusion_matrix(y_test, y_pred_LR)
print (cm_LR)

