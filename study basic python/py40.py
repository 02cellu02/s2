#classes
class point:
    def move(self):
        print('move')
    def draw(self):
        print('draw')

point1=point()#creating instance
point1.draw()
point1.x=10#attributes
point1.y=20
print(point1.x)
