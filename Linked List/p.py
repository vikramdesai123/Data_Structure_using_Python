class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class DoublyCircularLL:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def traversal(self):
        if self.head is None:
            print("Doubly circular linked list is empty")
        else:
            temp=self.head
        
            print(temp.data,end=" ")
            while temp.next is not self.head:
                temp=temp.next
                print(temp.data,end=" ")
             
    def reverseTraversal(self):
        print()
        if self.head is None:
            print("Doubly circular linked list is empty")
        else:
            temp=self.tail
            print(temp.data,end=" ")
            while temp is not self.head:
                temp=temp.prev
                print(temp.data,end=" ")
                
    
    def insertFirst(self,n):
        print()
        new=Node(n)
        
        if self.head is None:
            self.head=new
            self.tail=new
            self.head.prev=self.tail
            self.tail.next=self.head
        else:
            new.next=self.head
            new.prev=self.tail
            self.head.prev=new
            self.tail.next=new
            self.head=new
            
    def insertLast(self,n):
        print()
        new=Node(n)
        
        if self.head is None:
            self.head=new
            self.tail=new
            self.head.prev=self.tail
            self.tail.next=self.head                    
        else:
            new.prev=self.tail
            new.next=self.head
            self.tail.next=new
            self.head.prev=new
            self.tail=new             

    def insertAtAnyPosition(self,pos,n):
        print()
        new=Node(n)
        
        if self.head is None:
            self.head=new
            self.tail=new
            self.head.prev=self.tail
            self.tail.next=self.head 
        else:
            before=self.head
            after=self.head.next
            
            for i in range(1,pos-1):
                before=before.next
                after=after.next 
            new.prev=before
            new.next=after.next 
            before.next=new
            after.next.prev=new
            after=None
        
    def deleteFirst(self):
        print()
        
        if self.head is None:
            print("linked list is an empty")
        elif self.head==self.tail:
            self.head=None
        else:
            temp2=self.head.next
            
            temp2.prev=self.tail
            self.tail.next=temp2
            self.head=temp2

    def deleteLast(self):
        print()
        
        if self.head is None:
            print("linked list is an empty")
        elif self.head==self.tail:
            self.head=None
        else:
            temp=self.head
            
            while temp.next is not self.tail:
                temp=temp.next
            temp.next=self.head
            self.head.prev=temp
            self.tail=temp
    
    def deleteAtPosition(self,pos):
        print()
        
        if self.head is None:
            print("linked list is an empty")
        elif self.head==self.tail:
            self.head=None
        else:
            before=self.head
            after=self.head.next
            
            for i in range(1,pos-1):
                before=before.next
                after=after.next 
            before.next=after.next 
            after.next.prev=before
            
               

dcl=DoublyCircularLL()

n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)

dcl.head=n1
dcl.tail=n1
dcl.tail.next=dcl.head
dcl.head.prev=dcl.tail

dcl.tail.next=n2
dcl.tail=n2
dcl.tail.prev=n1
dcl.tail.next=dcl.head

dcl.tail.next=n3
dcl.tail=n3
dcl.tail.prev=n2
dcl.tail.next=dcl.head

dcl.tail.next=n4
dcl.tail=n4
dcl.tail.prev=n3
dcl.tail.next=dcl.head

dcl.traversal()
dcl.reverseTraversal()

dcl.insertFirst(5)
dcl.traversal()
dcl.reverseTraversal()

dcl.insertLast(45)
dcl.traversal()
dcl.reverseTraversal()

dcl.insertAtAnyPosition(5,35)
dcl.traversal()
dcl.reverseTraversal()

dcl.deleteFirst()
dcl.traversal()
dcl.reverseTraversal()

# dcl.deleteLast()
# dcl.traversal()
# dcl.reverseTraversal()

dcl.deleteAtPosition(4)
dcl.traversal()
dcl.reverseTraversal()