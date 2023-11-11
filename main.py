import pandas as pd
from sklearn import datasets
from sklearn import linear_model
import numpy as np
from sklearn.model_selection import train_test_split

df = pd.read_csv("data.csv")
unique_values = df['rps01'].unique()
print(unique_values)
