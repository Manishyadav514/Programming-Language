import pandas as pd
from sklearn.tree import DecisionTreeRegressor

file = "D:\project\Language-Python\modules\data.csv"
data = pd.read_csv(file)
data.describe()
# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)