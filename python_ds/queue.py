#using lists:
queue=[]
def push():
    print("enter the element")
    ele=input()
    queue.append(ele)
def pop():
    h=queue.pop(0)
    print("popped ele :"+h)
def show():
    print(queue)
while True:
    print("enter the choice 1.push 2.pop 3.show 4.exit ")
    x=int(input())
    if x==1:
        push()
    elif x==2:
        pop()
    elif x==3:
        show()
    else:
        break

#collection modules:

import collections
#adding on left side and removing at right side
q=collections.deque()
q.appendleft(10)
q.appendleft(20)
q.appendleft(30)
q.pop()
q.pop()
print(q)
#adding at right side and removing from left side
x=collections.deque()
x.append(3)
x.append(2)
x.append(1)
x.popleft()
print(x)


    
