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
    
def reverse_string(string):
    arr=stack()
    for i in string:
        arr.push(i)
    rev=''

    while not arr.is_empty():
        rev +=arr.pop()
    return rev

print(reverse_string("We will conquere COVID-19"))