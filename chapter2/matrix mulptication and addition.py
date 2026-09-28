import numpy as np
list1=[[2,3,4],[3,4,5]]
list2=[[4,5,6],[6,7,8]]

a=np.array(list1)*np.array(list2)
b=np.array(list1)+np.array(list2)
print("multiplication")
print(a)
print("addition")
print(b)
print("items in list1")
for i in list1:
    print(i)
