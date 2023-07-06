class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head=None
    def add_begin(self,data):
        newnode=Node(data)
        newnode.ref=self.head
        self.head=newnode
    def add_end(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
           n=self.head
           while n.ref is not None:
               n=n.ref
           n.ref=newnode
    def add_after(self,data,x):
        n=self.head
        while n.ref is not None:
            if n.data==x:
                break
            n=n.ref
        newnode=Node(data)
        newnode.ref=n.ref
        n.ref=newnode
    def add_before(self,data,x):
        if self.head is None:
            print("empty")
        if self.head.data==x:
            newnode=Node(data)
            newnode.ref=self.head
            self.head=newnode
        else:
            n=self.head
            while n.ref is not None:
                if n.ref.data==x:
                    break
                n=n.ref
            if n.ref is None:
                print("node not found")
            else:
                newnode=Node(data)
                newnode.ref=n.ref
                n.ref=newnode
    def insert_empty(self,data):
        if self.head is None:
            newnode=Node(data)
            self.head=newnode
        else:
            print("Linked list is not empty")
    def delete_begin(self):
        if self.head is None:
            print("linked list is empty") 
        else:
            self.head=self.head.ref
    def delete_end(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None
    def delete_bw(self,x):
        if self.head is None:
            print("linked list empty")
        if self.head.data==x:
            self.head=self.head.ref
        else:
            n=self.head
            while n.ref is not None:
                if n.ref.data==x:
                    break
                n=n.ref
            if n.ref is None:
                print("Node not present")
            else:
                n.ref=n.ref.ref
    def print_LL(self):
        n=self.head
        if n is None:
            print("Linked list is empty")
        while n is not None:
            print(n.data)
            n=n.ref


LL1=LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_after(30,30) 
LL1.add_before(5,20)
LL1.delete_bw(10)
LL1.print_LL()
