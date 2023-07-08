class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Circular_LL:
    def __init__(self):
        self.head=None
    def add_begin(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            n=self.head
            while n:
                if n.ref==self.head:
                    break
                n=n.ref
            n.ref=newnode
            newnode.ref=self.head
            self.head=newnode
    def add_end(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            n=self.head
            while n:
                if n.ref==self.head:
                    break
                n=n.ref
            n.ref=newnode
            newnode.ref=self.head
    def add_after(self,data,x):
         n=self.head
         while n:
             if n.data==x:
                 break
             n=n.ref
         newnode=Node(data)
         newnode.ref=n.ref
         n.ref=newnode
    def add_before(self,data,x):
        if self.head.data==x:
            newnode=Node(data)
            newnode.ref=self.head
            self.head.ref=newnode
            self.head=newnode     
        else:
            n=self.head
            while n:
                if n.ref.data==x:
                    break
                n=n.ref
            if n.ref is None:
                print("node not found")
            else:
                newnode=Node(data)
                newnode.ref=n.ref
                n.ref=newnode
    def delete_begin(self):
         if self.head is None:
             print("linked list is empty") 
         if self.head.ref is None:
             self.head=None
         else:
             n=self.head
             while n:
                 if n.ref==self.head:
                     break
                 n=n.ref
             n.ref=self.head.ref
             self.head=self.head.ref
    def print_LL(self):
        n=self.head
        if n is None:
            print("Linked list is empty")
        while n:
            print(n.data)
            n=n.ref


c1=Circular_LL()
c1.add_begin(10)
c1.add_begin(20)
c1.add_begin(30)
c1.print_LL()
            
        
                
        
