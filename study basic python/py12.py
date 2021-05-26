#String functions and methods
course='Python For Beginner'
print(len(course))#len:length of string;gen fn
print(course.upper())#uppercase;they are methods.
print(course.lower())#lowercase
print(course.find('F'))#returns index of first occuring of that character;
                       #returns -1 if character is not found;           
print(course.find('Beginner'))#returns index of first character;if not found then -1;
print(course.replace('For','for every'))#replace character or string if found.
print('Python 'in course)#returns true when substring is found  else false.