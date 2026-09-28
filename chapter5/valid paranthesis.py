prices=[7,1,5,3,6,4]
for i in range(len(prices)):
    buy=min(prices)
            
    ind = prices.index(buy)
    price=[]
    for j in range(ind+1,len(prices)):
        price.append(prices[j])
        sell=max(price)
        profit=sell-buy
        
print(profit)
stack=[]
def check(exp):
            open="([{"
            close=")]}"
            for char in exp:
                if char in open:
                    stack.append(char)
                elif char in close:
                    if not stack:
                        return False
                    elif stack:
                        return True
                    if open.index(stack.pop())!=open.index():
                        return False
                    elif open.index(stack.pop())==open.index():
                         return True
            print("False") 

c="()"     
print(check(c))

def duplicate(nums):    
    for i in nums:
        for j in nums:
            if nums[i]!=nums[j]:
                return False
            else:
                return True

   
            
       