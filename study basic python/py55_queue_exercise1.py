#https://www.youtube.com/watch?v=PJ4t2U15ACo&list=PLeo1K3hjS3uub3PRhdoCTY8BxMKSW7RjN&index=2&t=0s
#multi threading in python
'''Design a food ordering system where your python program will run two threads,

Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.
Use this video to get yourself familiar with multithreading in python

Pass following list as an argument to place order thread,

orders = ['pizza','samosa','pasta','biryani','burger']
This problem is a producer,consumer problem where place_order thread is producing orders whereas server_order thread is consuming the food orders. Use Queue class implemented in a video tutorial.
'''
import threading
import time
from collections import deque
class Queue:
    def __init__(self):
        self.buffer=deque()

    def enqueue(self,val):
        self.buffer.appendleft(val)
    
    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)

food_order_queue=Queue()
def place_order(orders):
    for elt in orders:
        print('place order:',elt)
        food_order_queue.enqueue(elt)
        time.sleep(0.5)

def serve_order():
    time.sleep(1)
    while not food_order_queue.is_empty():
        print('serve order: ',food_order_queue.dequeue())
        time.sleep(2)

if __name__=='__main__':
    order=['pizza','samosa','pasta','biryani','burger','cherry']
    t1=threading.Thread(target=place_order,args=(order,))
    t2=threading.Thread(target=serve_order)
    t1.start()
    t2.start()