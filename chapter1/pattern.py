row=4
col=4
#triangle of 7 rows
for i in range(row):
    for j in range(col):
        if j>=row-i-1 and j<=row+i-1:
            print("*", end="")
    print()
for i in range(row):
    for j in range(col):
        if j<=row-i-1 and j<=row+i-1:
            print("*", end="")
    print()

   
print("\"hello world\"")
  