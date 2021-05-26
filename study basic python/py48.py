#builtin modules-random module
import random#importing module
for i in range(3):
    print(random.random())#returns value btw 0 and 1
for i in range(3):
    print(random.randint(10,20))#returns arbitrary value btw 10 and 20(included)
#if u want to randomly choose something
members=['Cel','galdin','sheena','joy']
leader=random.choice(members)
print(leader)
