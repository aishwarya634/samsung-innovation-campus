#josephanance sequence using queue
def josephous_sequence(n,k):
    sequence=[]
    queue=[]
    for i in range (1,n+1):
        queue.append(i)
    i=1
    while len(queue)>0:
        item = queue.pop(0)
        if i%k==0:
            sequence.append(item)
        else:
            queue.append(item)
        i+=1
        
    return sequence
print(josephous_sequence(7,3))

#class queue with all its fuctions
class Queue:
    def __init__(self):
        self.queue=[]
    def is_match(self):
        return True if len(self.queue) ==0 else False
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        return None if self.is_empty else self.queue.pop(0)

class dequeue:
    def add_first(self,item):
        self.queue.append(0,item)
    def remove_first(self):
        self.queue.pop(0)
    def add_last(self,item):
        self.queue.append(item)
    def remove_last(self):
        if self.queue:
            self.queue.pop()

num=[10,30,20,60,50,40]
i=0
for n in num:
    for i in range(len(num)-1):
        if num[i]<num[i+1]:
            num[i],num[i+1]==num[i+1],num[i]
            i+=1
print(num[i])
s=[10,20,10,30,20]
y=len(s)
i=0
for i in range(y):
    for j in range(i+1,y):

        if s[i]==s[j]:
            n=1
print("not unique list") 

a=input("enter a string;")
b=list(a)
c=len(b)


for i in range(c):
    count=1
    for j in range(i+1,c):
        
        if b[i]==b[j]:
            count+=1
            b[j]=None
    if b[j] is not None:
        print(b[j],count)




def int_to_roman(num):
    table = {
        1000:'M', 900:'CM', 500:'D', 400:'CD',
        100:'C', 90:'XC', 50:'L', 40:'XL',
        10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'
    }
    result = ""
    for value, symbol in table.items():
        while num >= value:
            result += symbol
            num -= value
    return result

inte=int(input("enter a integer:"))
print(int_to_roman(inte))  
