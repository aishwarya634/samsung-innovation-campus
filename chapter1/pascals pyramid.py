#count=0
#for i in range(1,201):
    #if i%3==0 and i%7==0:
         #count+=1
         #print(i)
#print(count)
n=6
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(0,i+1):
        print(j,end="   ")
    print()
i=0
while 1<i<n+1:
    while j<n-i:
        print(" ",end="")
    while 1<j<i+1:
        print(j,end=" ")
        i+=1
#sum
n=-1
s=0
i=1
while i<=0:
    n=int(input("sumof numbers from 1 to",n))
    
for i in range(n+1):
    s=s+i
    print(s)
#rock paper scissors
