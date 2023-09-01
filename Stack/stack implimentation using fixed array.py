class Stack:
    def __init__(self,size):
        self.stack=[]
        self.size=size
        self.pointer=-1
        
    def isEmpty(self):
        return self.pointer==-1
    
    def isFull(self):
        return (self.pointer==self.size-1)
    
    def push(self,element):
        if self.pointer>=(self.size-1):
            raise Exception("stack is overfloww")
        else:
            self.stack.append(element)
            self.pointer+=1
    
    def pop(self):
        if self.pointer<=-1:
            raise Exception("stack is underfloww")
        else:
            value=self.stack[-1]
            self.stack=self.stack[:-1]
            self.pointer-=1
            print(value)
        
    def peek(self):
        print(self.stack[self.pointer])

s=Stack(size=5)

# s.push(10)
# s.push(20)
# s.push(30)
s.push(40)
s.push(50)
s.push(60)

s.pop()

# s.peek()


print(s.stack)