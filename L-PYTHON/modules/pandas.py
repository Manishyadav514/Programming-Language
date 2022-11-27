import pandas as pd

file = "D:\project\Language-Python\modules\data.csv"
data = pd.read_csv(file)
data.describe()