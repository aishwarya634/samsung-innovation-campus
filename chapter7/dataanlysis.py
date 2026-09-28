import pandas as pd
#train.csv
titanic = pd.read_csv("C:/Users/Aishwarya/Downloads/train.csv", skiprows=10)
print(type(titanic))
print(titanic.head(5))
print(titanic.info()) # gives metadata
print(titanic.describe()) #give descriptive satistic value

# skiprows and index_col cant be done together
titanic = pd.read_csv(
    "C:/Users/Aishwarya/Downloads/train.csv",
    index_col="Name"
)

print(titanic.head())



titanic = pd.read_csv("C:/Users/Aishwarya/Downloads/train.csv")

print(titanic.isnull().sum().sum())

import seaborn as sns
a=sns.load_dataset("titanic",cache=True)
print(a)

e=titanic.dropna()
print(e)