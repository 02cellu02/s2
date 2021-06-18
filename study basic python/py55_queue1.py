stock_price=[]
stock_price.insert(0,344)
stock_price.insert(0,34)
stock_price.insert(0,24)
stock_price.insert(0,65)
print(stock_price.pop())
#or 
from collections import deque
q=deque()
q.appendleft(5)
q.appendleft(53)
q.appendleft(52)
print(q.pop())