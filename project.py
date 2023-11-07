import pandas as pd

a = pd.read_csv("total_stars.csv")

#print(a.columns)
# 'Unnamed: 0', 'Star_name', 'Distance', 'Mass', 'Radius', 'Luminosity',
# 'Unnamed: 6', 'Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1'

a.drop(columns = ['Luminosity','Unnamed: 0','Unnamed: 6', 'Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1'], axis = 1, inplace = True)
b = a.dropna()
print(b.describe())
print(b.info())
print(b.dtypes)