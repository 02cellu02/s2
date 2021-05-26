class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_front(self,data):
        node=Node(data,self.head)
        self.head=node
    
    def print(self):
        if not self.head:
            print('empty list')
            return
        else:
            p=self.head
            s=''
            while p:
                s+=f'{p.data}---'
                p=p.next
            print(s)
    def insert_at_back(self,data):
        if not self.head:
            self.head=Node(data)
            return
        else:
            p=self.head
            while p.next:
                p=p.next
            p.next=Node(data)
            return
    def insert_all_values(self,data_list):
        for data in data_list:
            self.insert_at_back(data)
    
    def get_length(self):
        p=self.head
        c=0
        while p:
            c+=1
            p=p.next
        return c
    
    def remove_at_index(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")
        if index==0:
            self.head=self.head.next
            return
        c=0
        p=self.head
        while p:
            if c==index-1:
                p.next=p.next.next
                break
            p=p.next
            c+=1
    def insert_at(self,index,data):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")
        if index==0:
            self.insert_at_front(data)
            return
        p=self.head
        c=0
        while p:
            if c==index-1:
                node=Node(data,p.next)
                p.next=node
                break
            p=p.next
            c+=1

    def insert_after_value(self, data_after, data_to_insert):
        p=self.head
        while p:
            if p.data==data_after:
                node=Node(data_to_insert,p.next)
                p.next=node
                break
            p=p.next
        else:
            print('data_after not Found')
    
    def remove_by_value(self, data):
        if self.head.data == data:
            self.head = self.head.next
            return
        p=self.head
        while p:
            if p.next and p.next.data==data:
                p.next=p.next.next
                break
            p=p.next
        else:
            print('data not Found')


if __name__=='__main__':
    ll = LinkedList()
    ll.insert_all_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()

   
