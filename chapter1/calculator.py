a=int(input("enter number a:"))
b=int(input("enter number b:"))
print("1=addition")
print("2=substract")
print("3=multiplication")
print("4=division")
choice=int(input("enter the desired number of operation:"))
if choice== 1:
   c=a+b
   print(c)
elif choice== 2:
   c=a-b
   print(c)
elif choice== 3:
   c=a*b
   print(c)
elif choice== 4:
   c=a/b
   print(c)
else:
   print("invalid choice")
