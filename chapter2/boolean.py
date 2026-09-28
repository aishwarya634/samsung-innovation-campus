lis=[1,2,3,4]
for i in range(3):
    line =[]
    for j in range(3):
        line.append(j)
    
    print(line)
n=6
for i in range(0,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(0,i+1):
        print(j,end="   ")
    print()
list1=[1,2,3,4,5]
c=len(list1)
for i in range(0,c+1):
    line=[]
    for j in range(c-i):
        print(" ",end=" ")
    for j in range(0,i+1):
        line.append(j)
        print(j,end="   ")  
    print()

variable=[[10,20],[30,40],[50,60]]
print(variable[1][0])

listt=[2,3,4,6,5]
for i in listt:
    for j in range(1,5):
        print(i,end=" ")
    print()
list_ar=[[0]*4 for i in range(4)]
print(list_ar)

#f=open("hi.txt","r")
#f#.read()
#s=f.readline()[-1]
#print(s)

#f.close()

#multidimentional array
#n= int(input("enter the number:"))
n=4
arr=[[(i+j)%2 for i in range(n)]for j in range(n)]
for a in arr:
    print(a)

for i in range(n):
    print()
    for j in range(n):
        if (i+j)%2==0:
            print(1, end=" ")
        else:
            print(0,end=" ")

person={"first name":"david","last name":"doe","company":"samsung"}
for a,b in person.items():
    print(a ,":",b)

print("Select menu") 
print("1)check stock 2)warehousing 3) release 4) exit")
#n=int(input("enter your choice:"))
n=4
dic={"milk":2,"eggs":4}
if n==1:
    a=input("enter the iteam:")
    d=dic.get(a)
    if d==None:
        print("item not found")
    else:
        print("stock",d)
elif n==2:
    print("number of warehouse 3")
elif n==3:
    b=input("enter item:")
    e=dic.get(b)
    if e==None:
        print("item not found")
    else:
        print("stock",e-1)
elif n==4:
    print("program exited")

from collections import defaultdict
from email.policy import default


start_tup=(("2000","divsdi",'28404601'),("3000","doe",'732591'))
sett={}
for a,b,c in start_tup:
    sett[a]=[b,c]
    #d=[b,c]
    #print(a,":",d)
print(sett)
lst=["apple","orange","bannba"]
print(lst)
s=set(lst)
print(s)
s1={12,20,30,40}
s2={30,40,50,60}
print(s1|s2)
print(s1&s2)
print(s1-s2)
print(s1^s2)
num=20
d=[]
for i in range(2,num):
    if num%i!=0:
        d.append(i)
print(d)
my_list=[(1,2),(2,3),(4,5)]
a, b = map(int, input("Enter two integers: ").split())

if (a,b) in my_list:
        print("there is",n,"at the",a.index())
        
else:
        print("no such number in list")
