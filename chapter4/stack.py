stack=[10,20]
print(stack)
stack.append("a")
print(stack)
def push(stack,item):
    stack.append(item)
def pop(stack):
    
    return stack.pop()

print(stack)
push(stack,30)
print(stack)
pop(stack)
print(stack)


#def palindrome(stack):
 #   if stack[0]==stack[-1]:
  #      return False
   # return palindrome(stack[0:-1])

#if palindrome:
 #   print("stack is palindrome")
#else:
 #   print("stack is not palindrome")

 #palindrome code
s=['a','b','a']
p=[]
for i in s:
    a=s.pop()
    p.append(a)
if s==p:
    print("palindrome")
else:
    print("not")

def check(expersion):
    open="([{"
    close=")]}"
    
    for char in expersion:
        if char in open:
            stack.append(char)
        elif char in close:
            if  stack.is_empty:
                return False
            if open.index(stack.pop())!=close.index(char):
                return False
    return stack.is_empty

#match html tags using stack
#

#match html tags using stack and regular expression 
import re
def match_tags_regex(html):
    open_tags = re.findall(r'<([a-zA-Z]+)>', html)
    close_tags = re.findall(r'</([a-zA-Z]+)>', html)
    stack = []
    for tag in open_tags:
        stack.append(tag)
        return True
    for tag in close_tags:
        if not stack or stack.pop() != tag:
            return False
    return not stack
html="<h1> </h1> <li> </li> <p> </p>"
if match_tags_regex(html):
    print("Tags are balanced")
else:
    print("Tags are not balanced")