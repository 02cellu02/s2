#to find largest no in a list
list1=[1,3,2,8,4,3]
larg=list1[0]
for i in list1:
    if i>larg:
        larg=i
print(larg)