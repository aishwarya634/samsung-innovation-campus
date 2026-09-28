import pandas as pd
import numpy as np
#costum indexing
#creating series using list 1
marks = pd.Series([85, 72, 91,45,67],
                   index=["aish","rahul","rohit","ri","ro"])

print("multiplication",marks*2)
print(marks)
print(marks.values)
print(marks.index)
print(marks["aish"])


#can use dict in pd
#creating list using dictionary 2
veg={
    "panner":34,
    "potato":45,
    "peas":56}
vr=pd.Series(veg)
print(vr)

#calculations using pd
print("mean",marks.mean())
print("maximum",marks.max())
print("minimum",marks.min())
print("sum",marks.sum())
print("std",marks.std())
print("median",marks.median())
print("count",marks.count())


#Both the numpy and pandas
#creating list using numpy 3
k=np.arange(9,15)
g=pd.Series(k)
print(g)

#random in numpy
np.random.seed(0)
f=np.random.random(size=3)
c=pd.Series(f)
print(c)

#creating using scalar 4
d=pd.Series(2,index=["a","b","c"])
print(d)

#graph
import matplotlib.pyplot as plt
plt.plot(marks)
plt.show()