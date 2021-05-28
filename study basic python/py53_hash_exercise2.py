'''
nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
What was the temperature on Jan 9?
What was the temperature on Jan 4?
Figure out data structure that is best for this problem
'''
weather={}
with open("nyc_weather.csv",'r') as f:
    for line in f:
        token =line.split(',')
        try:
            date =token[0]
            temperature=int(token[1])
            weather[date]=temperature
        except:
            print("invalid temperature")

print(weather['Jan 9'])
print(weather['Jan 4'])

