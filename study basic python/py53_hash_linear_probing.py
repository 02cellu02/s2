class hashtable:
    def __init__(self):
        self.max=10
        self.arr=[None for i in range(self.max)]

    def get_hash(self,key):#our hash fn is sum of ascii values of key modulus 100
        sum=0
        for char in key:
            sum+=ord(char)#returns ascii value of character
        return sum%self.max

    def __setitem__(self,key,value):#to set the value of arr at index key to value
        h=self.get_hash(key)
        c=h
        while self.arr[h]:
            if self.arr[h][0]==key:
                self.arr[h]=(key,value)
                return
            if h==self.max-1:
                h=0
            else:
                h+=1
            if c==h:
                raise Exception("Hashmap full")
                return
        self.arr[h]=(key,value)

    def __getitem__(self,key):#here u can use arr[key] while calling instead p1.some_fn(key)
        h=self.get_hash(key)
        while self.arr[h]:
            if self.arr[h][0]==key:
                return self.arr[h][1]
            if h==self.max-1:
                h=0
            else:
                h+=1

    def __delitem__(self,key):#standard operators in python
        h=self.get_hash(key)
        while self.arr[h]:
            if self.arr[h][0]==key:
                self.arr[h]=None
                return
            if h==self.max-1:
                h=0
            else:
                h+=1

t = hashtable()
t["march 6"] = 20
t["march 17"] =  88
print(t.arr)
t["march 17"] = 29
print(t.arr)
t["nov 1"] = 1
print(t.arr)
t["march 33"] = 234
print(t.arr)
print(t["dec 1"])
print(t["march 33"])
t["march 33"] = 999
print(t.arr)
print(t["march 33"])
t["april 1"]=87
t["april 2"]=123
t["april 3"]=234234
print(t.arr)
t["april 4"]=91
t["May 22"]=4
t["May 7"]=47
print(t.arr)
del t["april 2"]
print(t.arr)
t["Jan 1"]=0
print(t.arr)