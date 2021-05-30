#list implementation
stack =[]
stack.append(3)
stack.append(13)
stack.append(23)
stack.append(34)
stack.append(12)
stack.append(38)
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
#the problem with list is that if the list is full and if we add, it will make a new list with increase in size by two times the current size
#so the size will be 3 times the original list
#and we have to copy elts to the new list.so its time waste so we will use LL.
