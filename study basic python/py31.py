#delete duplicate entries in list
numbers=[2,3,2,4,1,3,2,5,2,6,1]
n2=[]
for items in numbers:
    if items not in n2:
        n2.append(items)
print(n2)
