
n=23
l=[]
for i in range(1,n+1):
    if(n%i==0):
        l.append(i)

if len(l)>2:
    print(n,"com")
else:
    print(n,"prime")
num=3.1415926
#dictionary
print(f"real number:{num:10.3f}")
fruit_list={"apple":6000,"melon":7000,"banana":3000}
print("value of apple",fruit_list["apple"])
print("apple" in fruit_list)
print("orange" in fruit_list)
lis=[11,11,11,12,2,3,1]
print(lis.count(10))
ran=list(range(0,5,2))

print(ran)
even=list(range(1,11,2))
print(even)
list1=[3,4]
list2=[4,5]
print(list1+list2)

t1='a','b','c'
t2=('a','b','c')
t3=('a','b')
print(t1==t2)
print(t2+t3)
list1.sort()
print(list1)
tup=(2,3,4,56,56,56,2,3)
d=list(tup)

for a in tup:
    b=(tup.count(a))

    if b>2:
        print(a,b)
li=[[2,3,4],[4,5,6]]
print(li[0][2])
for item in li:
    print(item,"\n")
    for i,j,k in li:
        print(i,j,k)