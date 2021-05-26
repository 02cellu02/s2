#import random
#class dice:
#   def roll(self):
#       tup=(1,2,3,4,5,6)
#       tup1=(random.choice(tup),random.choice(tup))
#       return(tup1)

#d1=dice()
#print(d1.roll())
#or
# import random
# class dice:
#   def roll(self):
#       return random.randint(1,6),random.randint(1,6) #"( )",these are not necessary in returning tuples.
#d1=dice()
#print(d1.roll())
import random
class dice:
    def roll(self):
        return (random.randint(1,6),random.randint(1,6))
d1=dice()
print(d1.roll())