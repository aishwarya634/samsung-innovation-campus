
def bubble(a):
    n=len(a)
    for j in range(n-5):
        for i in range(n-1-j):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
    print(a)
x=[10,50,30,49,40,39]
bubble(x)

#with swap fuction

arr=[10,20,40,60,70,50]
b=len(arr)
for i in range(b-1):
    mi=i
    for j in range(i+1,b):
        if arr[j]<arr[mi]:
            mi=j
    arr[i],arr[mi]=arr[mi],arr[i]
print(arr)

#withou swap
f=[1,6,5,7,6]
s=[]
while f:
    c = min(f)
    f.remove(c)
    s.append(c)
print(s)


#can min b given a element to fint min range?
#insertion sort
def insertion(s):
    l=len(s)
    r=[]
    
    while len(s)>0:
        print(r,s)
        x=s.pop(0)
        j=len(r)-1
        while j>=0 and r[j]>x:
            j-=1
        r.insert(j+1,x)
    return r
z=[2,3,6,5,4,1]
insertion(z)

#quick sort
def quick(s,low,high):
    pivot=s[low]
    left,right=low+1,high
    while True:

       
        while left<=right and s[left]<=pivot:
            left+=1
        while left<=right and s[right]<=pivot:
            right-=1
        if left>right:
            break
        else:
            s[left],s[right]=s[right],s[left]
        pivotpoint=right
    s[low],s[pivotpoint]=s[pivotpoint],s[low]
    return pivotpoint
w=[10,40,55,30]
quick(w,0,len(w)-1)
print(w)