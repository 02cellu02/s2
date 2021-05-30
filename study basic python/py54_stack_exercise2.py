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

def match(close,open):
    brace={'[':']','{':'}','(':')'}
    return brace[open]==close

def is_balanced(string):
    arr=stack()
    for char in string:
        if char=='['or char=='(' or char=='{':
            arr.push(char)
        elif char==']'or char==')' or char=='}':
            if arr.is_empty():
                return False
            if not match(char,arr.pop()):
                return False
    return arr.is_empty()==True

print(is_balanced("({a+b})"))     
print(is_balanced("))((a+b}{"))   
print(is_balanced("((a+b))"))     
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
    