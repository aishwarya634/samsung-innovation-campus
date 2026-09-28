startValue=5
target=8
i=0
while target>startValue:
    if startValue%2==0:
        startValue=startValue*2
    else:
        startValue=startValue-1
    i+=1
print(i)

def duplicate(nums):
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):

            if nums[i] == nums[j]:
                return True

    return False


c=[2,2,3,4]
print(duplicate(c))

   
