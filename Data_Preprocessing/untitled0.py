# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 13:13:26 2018

@author: hp
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing dataset fro pd library
dataset = pd.read_csv('Data.csv')
#assining data set
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values
#taking care of missingn data
#from sklearn.preprocessing import Imputer
#now we need object of class Imuter
#imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
#imputer = imputer.fit(x[:, 1:3])
#x[:, 1:3] = imputer.transform(x[:, 1:3])




#data encoding as for mathmatical fn we need number 
#from sklearn.preprocessing import LabelEncoder
#labelencoder_dataset = LabelEncoder()
#labelencoder_dataset.fit_transform(dataset[:,0])