import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from category_encoders import OrdinalEncoder
from sklearn.pipeline import make_pipeline
from sklearn.tree import DecisionTreeClassifier
import pickle

df = pd.read_csv('DATA.csv')


target = np.array(df.iloc[:, 9])
features = np.array(df.iloc[:, 3:7])

X_train, X_val, y_train, y_val = train_test_split(features, target, test_size = 0.2, random_state = 2)

pipe = make_pipeline(
    OrdinalEncoder(), 
    DecisionTreeClassifier(max_depth=5, random_state=2)
)

model = pipe.fit(X_train, y_train)

with open('model.pkl', 'wb') as pickle_file:
    pickle.dump(model, pickle_file)