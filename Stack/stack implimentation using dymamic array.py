class Stack:
    def __init__(self,size):
        self.stack=[]
        self.size=size
        self.pointer=-1
    
    def push(self,element):
        if self.pointer==(self.size-1):
            self.resize()
        self.stack.append(element)
        self.pointer+=1
   
    
    def resize(self):
        newStack=[*self.stack]
        self.size=self.size*2
        self.stack=newStack
        
    def pop(self):
        if self.pointer==-1:
            raise Exception("stack is underfloww")
        else:
            value=self.stack[self.pointer]
            self.stack=self.stack[:-1]
            self.pointer-=1
            print(value)
        
    def peek(self):
        print(self.stack[self.pointer])
    
        
s=Stack(3)

s.push(10)
s.push(20)
s.push(30)

s.peek()

s.pop()

s.peek()


print(s.stack)