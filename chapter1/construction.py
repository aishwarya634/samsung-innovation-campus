st="hello world"
for ch in st:
    if ch in['a',"e","i","o","u"]:
        continue
    print(ch)
print("end")


#for i in range(2,3):
    #for j in range(1,11):
        #print(f"{i}x{j}={i*j:2d}")
# how to print multiplication table of all 9? 
j=1
i=9
while i in range(1,9):
    i+=1
    while j<11:
        print(f"{i}*{j}={j*i}")
        j=j+1
        i+=1
    print(f"{i}*{j}={j*i}")
print()

under_construction=True
while under_construction:
    respond=input("is the construction complelete")
    if respond=="yes":
        under_construction=False
print("escaped")
password=" "
while password!="python":
    password=input("enter password")
    print("password incorrect")
print("login succesful")
total=0
ans="yes"
while ans=="yes":
    num=int(input("enter the number:"))
    total+=num
    ans=input("enter yes or no:")
print(total)
nu=int(input("enter a number to find out weather a plidrome or not:"))
nu=nu//10
rev==nu