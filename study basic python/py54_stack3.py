from collections import deque
class stack:
    def __init__(self):
        self.list=deque()

    def push(self,val):
        self.list.append(val)

    def pop(self):
        return self.list.pop()
    
    def peek(self):
        return self.list[-1]
    
    def is_empty(self):
        return len(self.list)==0
    
    def size(self):
        return len(self.list)

s=stack()
s.push(5)
print(s.peek())
s.pop()
print(s.is_empty())
s.push(10)
print(s.size())