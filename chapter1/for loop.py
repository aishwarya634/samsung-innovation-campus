li=['apple','mango','grapes']
count=0
print(len(li))
for l in li:
    print(l)
    count+=1
    print(count,"\n")
    for ln in l:
        print(ln,end=",")
lis=[10,20,30]

s=0
print(sum(lis))
for n in lis:
    s=s+n
    print(s)
st="hello"
print(list(st))
