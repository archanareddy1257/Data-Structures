#using arrays:
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

    
