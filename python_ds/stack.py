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


#arrays
class stack:
    def __init__(self,size=10)->None:
        self.MAX=size
        self.stack=[]
        self.top=0
    def push(self,data):
        if self.top !=self.MAX:
            self.stack.append(data)
            self.top+=1
            return self.stack
        else:
            print("overflow")
    def pop(self):
        if self.top==0:
            print("underflow")
        else:
            self.top-=1
            return self.stack.pop()
    def __len__(self):
        return self.top
    def show(self)->str:
        s='Z|\t'
        for i in self.stack:
            print(i)
def main():
    s=stack(5)
    print(s.push(10))
    print(s.push(20))
    print(s.push(30))
    print(s.push(40))
    print(s.push(50))
    print(s.push(60))
    print(s.show())
    print(s.pop())
    print(len(s))
    print(s.pop())
    print(len(s))
if __name__=='__main__':
    main()
    

# Using Linked Lists:
class MyStack:
    #Function to push an integer into the stack.
    def __init__(self):
        self.head=None
        self.top=-1
        
    def push(self, data):
        # Add code here
        temp=StackNode(data)
        if self.head is None:
            self.head=temp
            self.top+=1
            return
        temp.next=self.head
        self.head=temp
        self.top+=1
        return
    #Function to remove an item from top of the stack.
    def pop(self):
        # Add code here
        if self.isEmpty():
            return -1
        temp=self.head
        self.head=self.head.next
        self.top-=1
        return temp.data
    def isEmpty(self):
        return self.top==-1
class StackNode:
    # Constructor to initialize a node
    def __init__(self, data):
        self.data = data
        self.next = None
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = MyStack()
        q = int(input())
        q1 = list(map(int, input().split()))
        i = 0
        while(i < len(q1)):
            if(q1[i] == 1):
                s.push(q1[i + 1])
                i = i + 2
            elif(q1[i] == 2):
                print(s.pop(), end=" ")
                i = i + 1
            elif(s.isEmpty()):
                print(-1)
        print()

# } Driver Code Ends
