#stack using lists
stack=[]
def push():
  if len(stack)==m:
    print("stack is full!")
  else:
    print("enter the element:")
    ele=int(input())
    stack.append(ele)
    print(stack)
def pop_element():
  if not stack:
    print("stack is empty!")
  else:
    e=stack.pop()
    print("removed element :",e)
    print(stack)
m=int(input("enter the stack limit:"))
while True:
  print("select the option 1.push\n 2.pop\n 3.exit")
  n=int(input())
  if n==1:
    push()
  elif n==2:
    pop_element()
  else:
    break



#using collections module
from collections import deque
sta=deque()
#push
sta.append(10)
sta.append(20)
sta.append(30)
#pop
sta.pop()

#queue modules
from queue import LifoQueue
stack=LifoQueue()
#push
stack.put(10)
stack.put(20)
stack.put(30)
#pop
stack.get()
#fixing stack length
s=LifoQueue(2)

