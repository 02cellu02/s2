#inheritance
class mammal:
    def walk(self):
        print("walk")

class dog(mammal):#u can use methods of mammals in dog also
    def bark(self):
        print("bark")

class cat(mammal):
    def annoy(self):
        print("annoy")

class mouse(mammal):
    pass#if we dont have anything to add

dog1=dog()
dog1.walk()
dog1.bark()
cat1=cat()
cat1.annoy()
mouse1=mouse()
mouse1.walk()
