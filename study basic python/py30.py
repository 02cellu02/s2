#list operations
numbers=[5,2,7,1,4]
numbers.clear()#removes everything ;just empty square bracket
numbers=[5,2,7,1,4,5]
numbers.append(20)#add 20 at end
numbers.insert(0,10)#1st index 2nd number to be inserted
numbers.remove(5)#removes the first occurence
print(numbers)#removes 5 from list
numbers.pop()#removes last elt
numbers.index(2)#gives index;if not found shows value error
print(5 in numbers)#gives true or false
print(numbers.count(5))#print no of elts with given value
numbers.sort()#sort
numbers.reverse()#reverse the list
number2=numbers.copy()#copy list independently
