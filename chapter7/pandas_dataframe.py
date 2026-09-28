import pandas as pd
# creating dataframe using dict
data = {
    "Name": ["Aisha", "Rahul", "Priya"],
    "Age": [18, 19, 18],
    "Marks": [85, 72, 91]
    
}
# changing index
df = pd.DataFrame(data,index=["a","b","c"])

print(df)
#for one column one bracket okay
print(df["Name"])

#for multiple columns double brakects
print(df[["Name", "Marks"]])


print(df.iloc[0])   # passing the position of the integer
print(df.loc["a"])  #for costum index passing the label
print(df.iloc[0:2]) # both 0 and 1 #last is not included
print(df.iloc[1,2])  # row 1 aand column 2
print(df.loc["a":"b"]) # last is included
#print(df.loc[0,1]) cant do this or this print(df.loc["a","b"])

#filtering
print(df[df["Marks"]>80])
print(df[df["Age"]!=18])
print(df[df["Marks"]==80])
print(df[df["Marks"] < 80])
#and
print("bool_and",df[
    (df["Age"] == 18) &
    (df["Marks"] > 80)])
#or
print("bool or",df[
    (df["Age"] == 18) |
    (df["Marks"] > 80)
])

#adding a new column
df["passed"]=True
print(df)
df["Pa"] = df["Marks"] >= 90
print(df)

#changing the column
d=df["Marks"]=df["Marks"]+5
print(d)
df["Pa"] = df["Marks"] >= 90
print(df)

#deleting a column
#axis=0 is index and asix=1 is column
df.drop("passed", axis=1, inplace=True)
print(df)

#dataframe fuction
print(df.head())
print(df.tail())
print(df.describe())
print(df.info())

#extracting info from csv file
#d=pd.read_csv("movies.csv") # this gives only one series
#print(d)

#to display all the columns and rows
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 2000)
pd.set_option("display.max_colwidth", None)
pd.set_option("display.expand_frame_repr", False)

d = pd.read_csv("movies.csv") # or u can add the path of the csv file

print(d)
print(d.head())
print(d.tail())
print(d.describe())
print(d.info())
print(d.columns)

print(d.index)
print(d.dtypes)
print(d.shape)
d.columns = d.columns.str.strip()


#creating csv file
df.to_csv("student.csv", index=False)
print(df)

# creating a dataframe manually
data={"col1":[1,2,3,4],"col2":["a","b","c","d"]}
print(pd.DataFrame(data=d))
h=pd.DataFrame(data,columns=[1,2]) # changing both index and columns
print(h)

# using rename
print(h.rename(index={0: "new index0"}, inplace=True))
print(h)
#creating dataframe using series
s1=[1,2,3,4]
s2=["a","b","c","d"]
n=pd.Series(s1,index=["t","y","r","w"])
f=pd.Series(s2,index=["s","f","g","h"])
q={"one":n,"two":f}
print(q)

#train.csv
titanic = pd.read_csv("C:/Users/Aishwarya/Downloads/train.csv")
print(type(titanic))
print(titanic.head(0))
print(titanic.info()) # gives metadata
print(titanic.describe()) #give descriptive satistic value