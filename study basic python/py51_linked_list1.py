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

            


if __name__=='__main__':
    l1=LinkedList()
    l1.insert_at_front(5)
    l1.insert_at_front(89)
    l1.insert_at_back(10)
    l1.print()
    l2=LinkedList()
    l2.insert_all_values([1,2,3,7,4,5])
    l2.print()
    print(l2.get_length())
    l3=LinkedList()
    l3.insert_all_values(['cel','gal','she','joy'])
    l3.remove_at_index(2)
    l3.print()
    l3.insert_at(2,'sheena')
    l3.print()