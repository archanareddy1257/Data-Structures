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

# Using 2 stacks
def Push(x,stack1,stack2):
    while len(stack1)!=0:
        stack2.append(stack1[-1])
        stack1.pop()
    stack1.append(x)
    while len(stack2)!=0:
        stack1.append(stack2[-1])
        stack2.pop()
#Function to pop an element from queue by using 2 stacks.
def Pop(stack1,stack2):
    #code here
    if len(stack1)==0:
        return -1
    x=stack1[-1]
    stack1.pop()
    return x
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        qry=int(input())
        qtyp_qry=list(map(int, input().strip().split()))
        
        i=0
        stack1=[]
        stack2=[]
        while i <len(qtyp_qry):
            #print(i)
            if qtyp_qry[i]==1:
                Push(qtyp_qry[i+1],stack1,stack2)
                #print(i)
                i+=2
            else:
                print(Pop(stack1,stack2),end=' ')
                i+=1
                
        print()
# } Driver Code Ends
    
