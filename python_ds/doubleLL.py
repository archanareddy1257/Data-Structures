class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DoubleLL:
    def __init__(self):
        self.head=None
    def add_begin(self,data):
        if self.head is None:
            newnode=Node(data)
            self.head=newnode
        else:
            newnode=Node(data)
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode
    def add_end(self,data):
        n=self.head
        if self.head is None:
            newnode=Node(data)
            self.head=newnode
        else:
            while n.next is not None:
                n=n.next
            newnode=Node(data)
            n.next=newnode
            newnode.prev=n
    def add_after(self,x,data):
        newnode=Node(data)
        if self.head is None:
            print("linked list is empty")
        else:
            if self.head.data==x:
                self.head.next=newnode
                newnode.prev=self.head
            else:
                n=self.head
                while n is not None:
                    if n.data==x:
                        break
                    n=n.next
                if n is None:
                    print("given node is not present")
                newnode=Node(data)
                newnode.next=n.next
                newnode.prev=n
                if n.next is not None:
                     n.next.prev=newnode
                     n.next=newnode
    def add_before(self,x,data):
        if self.head.data==x:
                self.head.next=newnode
                newnode.prev=self.head
        else:
            n=self.head
            while n is not None:
                if n.data==x:
                    break
                n=n.next
            if n is None:
                print("given node is not present")
            else:
                newnode=Node(data)
                newnode.next=n
                newnode.prev=n.prev
                if n.prev is not None:
                    n.prev.next=newnode
                else:
                    self.head=newnode
                n.prev=newnode  
                
    def insert_empty(self,data):
        if self.head is None:
            newnode=Node(data)
            self.head=newnode
        else:
            print("linked list is not empty")    
    def print_LL(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.next
    def delete_begin(self):
        if self.head is None:
            print("Linked list is empty")
        if self.head.next is None:
            self.head=None
        else:
            self.head=self.head.next
            self.head.prev=None
    def delete_end(self):
        if self.head is None:
            print("Linked list is empty")
        if self.head.next is None:
            self.head=None
        else:
            n=self.head
            while n.next is not None:
                if n.next.next==None:
                    break
                n=n.next
            n.next=None
    def delete_bw(self,key):
         if self.head is None:
            print("Linked list is empty")
         if self.head.next is None:
             if seld.head.data==key:
                 self.head=None
             print("node is not found")
         if self.head.data==key:
             self.head=self.head.next
             self.head.prev=None
         else:
             n=self.head
             while n.next is not None:
                 if n.next==key:
                     break
                 n=n.next
             if n.next is not None:
                 n.next.prev=n.prev
                 n.prev.next=n.next
             else:
                 if n.data==key:
                     n.prev.next=None
                 else:
                     print("node not found")
         
             
             
    def printrev_LL(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n.next is not None:
                n=n.next
                print("\t")
            while n is not None:
                print(n.data)
                n=n.prev


d1=DoubleLL()
d1.add_begin(20)
d1.add_begin(10)
d1.add_end(30)
d1.add_after(20,40)
d1.add_before(30,50)
d1.delete_begin()
d1.delete_end()
d1.delete_bw(40)
d1.print_LL()
d1.printrev_LL()
            
