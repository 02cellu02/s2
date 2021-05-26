class hashtable:
    def __init__(self):
        self.max=10
        self.arr=[[] for i in range(self.max)]#we will be storing both index and key

    def get_hash(self,key):#our hash fn is sum of ascii values of key modulus 100
        sum=0
        for char in key:
            sum+=ord(char)#returns ascii value of character
        return sum%self.max
    
    #def add(self,key,value):
    #    h=self.get_hash(key)
    #   self.arr[h]=value
    #or u can use below fn 

    def __setitem__(self,key,value):#to set the value of arr at index key to value
        h=self.get_hash(key)  #here u can use like arr[key]=value to call
        flag=False
        for idx,element in enumerate(self.arr[h]):#
            if len(element)==2 and element[0]==key:
                self.arr[h][idx]=(key,value)
                flag =True
                break
        if not flag:
            self.arr[h].append((key,value))

    def __getitem__(self,key):#here u can use arr[key] while calling instead p1.some_fn(key)
        h=self.get_hash(key)
        for elt in self.arr[h]:
            if elt[0]==key:
                return elt[1]
        #when u did not return anything python default returns None
    
    def __delitem__(self,key):#standard operators in python
        h=self.get_hash(key)
        for idx,element in enumerate(self.arr[h]):#
            if len(element)==2 and element[0]==key:
                del self.arr[h][idx]
                return

t=hashtable()
t['march 6']=120
t['march 6']=78
t['march 8']=67
t['march 9']=4
t['march 17']=459
print(t.arr)
print(t['march 6'])
#del t['march 1']
print(t['march 17'])
del t['march 17']
print(t.arr)