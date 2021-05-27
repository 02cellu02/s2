'''
(1) nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,

  (a) What was the average temperature in first week of Jan

  (b) What was the maximum temperature in first 10 days of Jan

  Figure out data structure that is best for this problem'''
weather=[]
with open("nyc_weather.csv","r") as f:
    for line in f:
        token =line.split(',')
        try:
            temp=int(token[1])
            weather.append(temp)
        except:
            print('invalid temperature')
print(weather)
#a
print(f'average temp of first week= {sum(weather[0:7])/len(weather[0:7])}')
print(f'maximum temp of first 10 days ={max(weather[0:10])}')