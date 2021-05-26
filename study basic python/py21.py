#pb
#while loop can also have else part;
#it will execute when while loop is executed successfully without an immediate break
#i.e no sudden breaks,in below pgm if guess is 9 then it breaks now else part willnot execute
i=3
while i:
    guess=int(input('Guess:'))
    if guess==9:
        print('u win')
        break
    i-=1
else:
    print('all 3 guesses were wrong')
    
    
