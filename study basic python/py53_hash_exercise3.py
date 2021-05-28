poem={}
with open('poem.txt','r') as f:
    for line in f:
        tokens= line.split(' ')
        for i in tokens:
            if i in poem:
                poem[i]+=1
            else:
                poem[i]=1
            
print(poem)
print(poem['diverged'])
print(poem['in'])
print(poem['I'])
