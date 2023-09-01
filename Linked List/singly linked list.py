class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class SinglyLL:
    def __int__(self):
        self.head=None
        
    
    def traversal(self):
        
        temp=self.head
        
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next
            

    def insertion_at_B(self,n):
        b=Node(n)
        
        temp=self.head
        b.next=temp
        self.head=b

    
    def insertion_at_L(self,n):
        
        l=Node(n)
        
        temp=self.head
        
        while temp.next is not None:
            temp=temp.next
        temp.next=l
        l.next=None
        
    def insertion_at_A(self,pos,n):

        a=Node(n)
        
        prv=self.head
        nxt=self.head.next
        
        for i in range(1,pos-1):
            prv=prv.next
            nxt=nxt.next
        prv.next=a
        a.next=nxt
    
    def delete_at_B(self):
        print()
        temp=self.head
        
        self.head=temp.next
        temp.next=None   
        
    def delete_at_L(self):
        prv=self.head
        nxt=self.head.next
        
        while nxt.next is not None:
            prv=prv.next
            nxt=nxt.next
        prv.next=None
        
    def delete_at_A(self,pos):
        prv=self.head
        nxt=self.head.next
        
        for i in range(1,pos-1):
            prv=prv.next
            nxt=nxt.next 
        prv.next=nxt.next 
        
    # def reverse(self):
    #     prev = None
    #     current = self.head
    #     while(current is not None):
    #         next = current.next
    #         current.next = prev
    #         prev = current
    #         current = next
    #     self.head = prev
    
    def searchNode(self,n):
        temp=self.head
        
        while temp is not None:
            if temp.data==n:
                return True
            temp=temp.next
            
    
          
        
sll=SinglyLL()

n1=Node(5)
sll.head=n1

n2=Node(10)
n1.next=n2

n3=Node(15)
n2.next=n3

n4=Node(20)
n3.next=n4

print("Original LL:",end=" ")
sll.traversal()
print()

# sll.insertion_at_B(555)
# print("LL after inserting element at beginning:",end=" ")
# sll.traversal()
# print()

# sll.insertion_at_L(5555)
# print("LL after inserting element at end:",end=" ")
# sll.traversal()
# print()

# sll.insertion_at_A(5,17)
# print("LL after inserting element at given position:",end=" ")
# sll.traversal()
# print()

# sll.delete_at_B()
# print("LL after deleting element from Beginning:",end=" ")
# sll.traversal()
# print()


# sll.delete_at_L()
# print("LL after deleting element from last:",end=" ")
# sll.traversal()
# print()

# sll.delete_at_A(4)
# print("LL after deleting element from given position:",end=" ")
# sll.traversal()
# print()

# sll.reverse()
# print("LL after reversing:",end=" ")
# sll.traversal()

if sll.searchNode(15):
    print("yess")
else:
    print("no")
