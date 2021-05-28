class hashtable:
    def __init__(self):
        self.max=100
        self.arr=[None for i in range(self.max)]

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
        self.arr[h]=value

    def __getitem__(self,key):
        h=self.get_hash(key)   #here u can use arr[key] while calling instead p1.some_fn(key)
        return self.arr[h]
    
    def __delitem__(self,key):#standard operators in python
        h=self.get_hash(key)
        self.arr[h]=None

t=hashtable()
t['march 6']=130
t['march 1']=20
t['dec 17']=27
print(t['march 6'])
del t['march 1']
print(t['march 1'])

