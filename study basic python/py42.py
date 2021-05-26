class person:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print(f'{self.name}, please talk')
    

p1=person('Celestine JOY')
print(p1.name)
p1.talk()
