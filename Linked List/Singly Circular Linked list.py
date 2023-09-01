class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class singlyCicularLL:
    def __init__(self):
        self.head=None
        self.tail=None
        
        
    def traversal(self):
        temp=self.head
        
        if temp is None:
            print("circular linked list is empty")
        else:
            print(temp.data,end=" ")
            while (temp.next!=self.head):
                temp=temp.next 
                print(temp.data,end=" ")
                
    
    def insertionAtFirst(self,n):
        print()
        f=Node(n) 
        
        if self.head is None:
            self.head=f
            self.tail=f
            self.tail.next=self.head   
        else:
            f.next=self.head
            self.tail.next=f
            self.head=f
                      
    def insertAtLast(self,n):
        print()
        l=Node(n)            
        
        if self.head is None:
            self.head=l
            self.tail=l
            self.tail.next=self.head
        else:
            self.tail.next=l
            l.next=self.head
            self.tail=l        

    def insertAtPosition(self,pos,n):
        print()
        a=Node(n)
        
        if self.head is None:
            self.head=a
            self.tail=a
            self.tail.next=self.tail
        else:
            before=self.head
            after=self.head.next
            for i in range(1,pos-1):
                before=before.next
                after=after.next 
            before.next=a
            a.next=after

    def deleteFirst(self):
        print()
        if self.head is None:
            print("linked list is empty")
        else:
            if self.head==self.tail:
                self.head=None
            else:
                temp=self.head
                
                self.head=temp.next
                temp=None
                self.tail.next=self.head
                
            
    def deleteLast(self):
        print()
        if self.head is None:
            print("linked list is empty")
        else:
            if self.head==self.tail:
                self.head==None
            else:
                temp=self.head
                while temp.next is not self.tail:
                    temp=temp.next
                self.tail=None
                self.tail=temp
                self.tail.next=self.head
            
            
    def deleteAny(self,pos):
        print()
        if self.head is None:
            print("linked list is empty")
        else:
            if self.head==self.tail:
                self.head=None
            else:
                before=self.head
                after=self.head.next
                
                for i in range(1,pos-1):
                    before=before.next
                    after=after.next
                
                before.next=after.next
                after=None
    
        

scl=singlyCicularLL()

n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n5=Node(50)

scl.head=n1
scl.tail=n1
scl.tail.next=scl.head

scl.tail.next=n2
scl.tail=n2
scl.tail.next=scl.head

scl.tail.next=n3
scl.tail=n3
scl.tail.next=scl.head

scl.tail.next=n4
scl.tail=n4
scl.tail.next=scl.head

scl.tail.next=n5
scl.tail=n5
scl.tail.next=scl.head

scl.traversal()

scl.insertionAtFirst(5)
scl.traversal()

scl.insertAtLast(55)
scl.traversal()

scl.insertAtPosition(5,35)
scl.traversal()

scl.deleteFirst()
scl.traversal()

scl.deleteLast()
scl.traversal()

scl.deleteAny(4)
scl.traversal()