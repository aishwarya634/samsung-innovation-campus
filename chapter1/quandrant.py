x=int(input("enter the x point:"))
y=int(input("enter the y point:"))
if x>0 and y>0:
    print("1st quadrant")
elif x<0 and y>0:
    print("2nd quadrant")
elif x<0 and y<0:
    print("3rd quadrant")
elif x>0 and y<0:
    print("4th quadrant")
print(list(range(50)))