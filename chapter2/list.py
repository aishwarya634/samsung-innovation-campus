
person1=["cavid doe",20,1,100.0,100.00]
person2=["john",25,1,170.0,100.0]
person3=["joh",27,1,130.0,110.0]
person4=["jo",26,1,172.0,102.0]
person_list=person1+person2+person3+person4
print(person_list)
n_persons=int(len(person_list)/5)
h_sum=0.0
for h in person_list[3::5]:
    h_sum+=h
average_h = float(h_sum)/n_persons
print(str(average_h))
#import numpy  for addition of list

fruit=['bannana','apple','kiwi']
print(fruit)
mixed_list=[100,200,300,'apple']
print(mixed_list)

# if use numpy it will be lot easier

#import numpy as np
#age=np.person_list
#print(age[1])

#import pandas as p
#a=p.person_list
#print(a)
n_list=[10,20,30,40]
print(n_list)
print(n_list.pop())
print(n_list)
#give a list start value is 3 and end value is 7
list=['3','4','5','6','7']

# y dont they hv back cameras on laptops
print(list[-7:])

list=[2,3,5,7]
list.append(11)
list1=[3,5,7]
list2=[2,3,4,5,6]

num = int(input("Enter a number: "))

if num <= 1:
    print("Neither prime nor composite")
else:
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        print("Prime number")
    else:
        print("Composite number")