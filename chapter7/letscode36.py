import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# STEP 1
tvsales = pd.read_csv(
    "C:/Users/Aishwarya/OneDrive/Documents/sic/chap 7/carssales.csv"
)

print(tvsales.head(10))
print(tvsales.info())
print(tvsales.describe())


# STEP 2
df = tvsales[["Sales", "Price", "CompPrice"]]

print(df.head())


# STEP 3
high_tvsales = tvsales[tvsales["Sales"] > 10]

print(high_tvsales.head())

rank = high_tvsales["ShelveLoc"].value_counts()

print(rank)

print(high_tvsales["ShelveLoc"].unique())


# STEP 4
good_shelf = high_tvsales[
    high_tvsales["ShelveLoc"] == "Good"
]

print(good_shelf.shape)


# STEP 5
medium_list = high_tvsales[
    high_tvsales["ShelveLoc"] == "Medium"]

medium = medium_list.reset_index(
    drop=True,
    inplace=False)

print(medium)


# STEP 6
x = tvsales["Price"]
y = tvsales["Sales"]
plt.scatter(x, y, color="red", alpha=0.5)

plt.show()


# CORRELATION
cor = tvsales.corr(
    method="pearson",
    numeric_only=True
)

print(cor)


# HEATMAP # how do u know its heatmap itslef like where did they wrote 
plt.matshow(cor)

plt.colorbar()

plt.show()
plt.figure(figsize=(8,6))
sns.heatmap(cor,annot=True)
plt.show()