# -*-coding:utf8-*-

import numpy as np
import pandas as pd

from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

imputer = Imputer(missing_values = "NaN", strategy = "mean", axis = 0)
dataset = pd.read_csv('dataset/data.csv')
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:, 3].values

imputer = imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])

labelencoder_x = LabelEncoder()
x[:, 0] = labelencoder_x.fit_transform(x[:, 0])
onehotencoder = OneHotEncoder(categorical_features=[0])
x = onehotencoder.fit_transform(x).toarray()
print(x)