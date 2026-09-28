
#squareof 3 rows and 3 columns
row=input("Enter the number of rows: ")
col=input("Enter the number of columns: ")
col= int(col)
row= int(row)
# move right fill the box
sp={(0,0),(1,0),(2,0),(3,0)}
#if row is 1 and col is 2 it shd be &
for i in range(row):
    for j in range(col):
        if (i,j) in sp:
            print("1", end=" ")
        else:
            print("*", end=" ")
    print()
print('''hello
 world''')
print("world"+str(1))
for _ in range(3):
    print("hi")