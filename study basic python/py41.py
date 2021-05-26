#class
class point:
    def __init__(self,x,y):#constructor
        self.x=x
        self.y=y

    def move(self):
        print('move')
    def draw(self):
        print('draw')

point1=point(2,3)
print(point1.y)