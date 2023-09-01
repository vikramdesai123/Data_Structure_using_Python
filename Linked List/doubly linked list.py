class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
        
class DoublyLL:
    def __init__(self):
        self.head=None
        
    def forward_traversal(self):
        temp=self.head
        
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next
        
        
    def backward_traversal(self):
        print()
        temp=self.head
        
        while temp.next is not None:
            temp=temp.next
            
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.prev  
          

    def insertion_at_first(self,n):
        print("Doubly linked list after insertion at first:")
        f=Node(n)
        
        temp=self.head
        
        f.next=temp
        temp.prev=f
        self.head=f

    def insertion_at_last(self,n):
        print("Doubly linked list after insertion at last:")
        l=Node(n)
        
        temp=self.head
        
        while temp.next is not None:
            temp=temp.next
        l.prev=temp
        temp.next=l

    def insertion_at_anyposition(self,pos,n):
        print("Doubly linked list after insertion given position:")
        a=Node(n)
        
        prv=self.head
        nxt=self.head.next
        
        for i in range(1,pos-1):
            prv=prv.next
            nxt=nxt.next 
        a.prev=prv
        a.next=nxt
        prv.next=a
        nxt.prev=a
    
    def deletion_at_first(self):
        print("Doubly linked list after deletion at first:")   
        
        temp1=self.head
        temp2=self.head.next
        
        temp2.prev=None
        self.head=temp2 
        
    def deletion_at_last(self):
        print("Doubly linked list after deletion at last:")   
        
        temp1=self.head
        temp2=self.head.next
        
        while temp2.next is not None:
            temp1=temp1.next
            temp2=temp2.next 
        temp1.next=None

    def deletion_at_position(self,pos):
        print("Doubly linked list after deletion at specific position:")
        
        temp1=self.head
        temp2=self.head.next
        
        for i in range(1,pos-1):
            temp1=temp1.next
            temp2=temp2.next 
        temp1.next=temp2.next
        temp2.next.prev=temp1
        temp2.next=None
        temp2.prev=None
        
    def searchNode(self,n):
        
        temp=self.head
        
        while temp is not None:    
            if temp.data==n:
                return True
            temp=temp.next    


dll=DoublyLL()

n1=Node(10)
dll.head=n1


n2=Node(20)
n1.next=n2
n2.prev=n1

n3=Node(30)
n2.next=n3
n3.prev=n2

print("Original doubly linked list:")
dll.forward_traversal()
print()
print("Original doubly linked list after reversing:",end="")
dll.backward_traversal()
print()
print()

dll.insertion_at_first(5)
dll.forward_traversal()
dll.backward_traversal()
print()
print()

dll.insertion_at_last(35)
dll.forward_traversal()
dll.backward_traversal()
print()
print()

dll.insertion_at_anyposition(4,25)
dll.forward_traversal()
dll.backward_traversal()
print()
print()

dll.deletion_at_first()
dll.forward_traversal()
dll.backward_traversal()
print()
print()

dll.deletion_at_last()
dll.forward_traversal()
dll.backward_traversal()
print()
print()

dll.deletion_at_position(3)
dll.forward_traversal()
dll.backward_traversal()
print()
print()

#searching node in linked list
if dll.searchNode(0):
    print("yess,entered node is present.")
else:
    print("noo,entered node is not present.")