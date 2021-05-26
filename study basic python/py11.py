#formatted stirng
#print John [Smith] is a coder using formatted stirng
first='John'
last='Smith'
message=first+' ['+last+'] is a coder'#normal way
mesg=f'{first} [{last}] is a coder'#formatted string
print(message)
print(mesg)
