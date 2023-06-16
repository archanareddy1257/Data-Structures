#arrays
def fun(arr,n,t):
    for i in range(n):
        if arr[i]==t:
            print(i)
    return -1
        

n=int(input("enter the size of array:"))
print("Enter array elements:")
arr=[]
for i in range(1,n+1):
    ele=int(input())
    arr.append(ele)
t=int(input("enter the target variable:"))
fun(arr,n,t)
#Linked list:
class LinkedList:
    def __init__(self):
        self.head=None
    def print(self):
        if self.head is None:
            print("empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
    def add_end(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=newnode
    def search(self,x):
        if self.head is None:
            print("empty")
        else:
            n=self.head
            while n is not None:
                if x==n.data:
                    print("yes")
                n=n.ref
        

LL1=LinkedList()
LL1.add_end(10)
LL1.add_end(20)
LL1.add_end(30)
LL1.search(45)
