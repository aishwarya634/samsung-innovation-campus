import ast
num=ast.literal_eval(input())
traget=int(input("traget:"))

a=len(num)

for i in range(a):
    for j in range(i+1,a):
        if num[i]+num[j]==traget:
            print([num[i],num[j]])

#multiway merge
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
        
    s[low],s[right]=s[right],s[low]
    return right
w=[10,40,55,30]
quick(w,0,len(w)-1)
print(w)

