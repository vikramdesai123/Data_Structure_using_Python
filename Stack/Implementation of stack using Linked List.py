class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
        
class Stack:
    def __init__(self) -> None:
        self.head=None
    
    def isEmpty(self):
        if self.head==None:
            print("stack is empty")
        else:
            print("Noo")
    def push(self,element):
        new=Node(element)
        if self.head:
            new.next=self.head
            self.head=new
        else:
            self.head=new
    
    def pop(self):
        if self.head:
            data1=self.head.data
            self.head=self.head.next
            return data1
        else:
            raise Exception("Stack is underflow")
    
    def peek(Self):
        if Self.head:
            return Self.head.data
        else:
            raise Exception("Stack is underfloww")

s=Stack()

s.push(10)
s.push(20)
print(s.peek())
print(s.pop())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Stack:
#     def __init__(self):
#         self.head = None

#     def is_empty(self):
#         return self.head == None

#     def push(self, data):
#         if self.head:
#             new_node = Node(data)
#             new_node.next = self.head
#             self.head = new_node
#         else:
#             self.head = Node(data)

#     def pop(self):
#         if self.head:
#             data = self.head.data
#             self.head = self.head.next
#             return data
#         else:
#             raise Exception('Stack underflow')

#     def peek(self):
#         if self.head:
#             return self.head.data
#         else:
#             raise Exception('Stack underflow')

# stack = Stack()
# print(stack.is_empty())
# stack.push(5)
# stack.push(9)
# stack.push(6)
# print(stack.pop())
# print(stack.peek())
# stack.push(5)
# print(stack.is_empty())
        