# import math
# how to print in table formate
# 3 digit hunderend term is 3 or not 
item_no=int(input("enter the item number:"))


if item_no<=4:
    quantity = int(input("enter the quantity:"))
    if item_no==1:
        print("fruit=apple")
        price=5000
        total_price=quantity*price
        print("total price",total_price)
    elif item_no==2:
        print("fruit=grape")
        price=6000
        total_price=quantity*price
        print("total price",total_price)
    elif item_no==3:
        print("fruit=melon")
        price=8000
        total_price=quantity*price
        print("total price",total_price)
    elif item_no==4:
        print("fruit=orange")
        price=2000
        total_price=quantity*price
        print("total price",total_price)
else:
    print("item not avilable")


