#using inheritance
from collections import deque
class Queue(deque):
    def enqueue(self,val):
        self.appendleft(val)
    
    def dequeue(self):
        return self.pop()

    def is_empty(self):
        return len(self)==0
    
    def size(self):
        return len(self)

pq=Queue()
pq.enqueue(1)
pq.enqueue(5)
pq.enqueue(8)
pq.enqueue(12)
print(pq.dequeue())
print(pq.size())
print(pq.is_empty())