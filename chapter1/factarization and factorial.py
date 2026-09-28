#factarization
n=5
count=0
temp=int()
for i in range(n,0,-1):
    if n%i==0:
        print(i ,end=" * ")
    count+=1
#factorial
fact=1
for i in range(1,n+1):
    fact=fact*i
    print(fact)
numbers=[11,22,33,44]
for n in numbers :
    print(n)

    