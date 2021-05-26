#handle error
try:
    age=int(input('<'))
    income=20000
    risk=income/age#age cant be zero
    print(age)
except ZeroDivisionError:
    print("age can't be Zero")
except ValueError:#happens while converting non numerical value to integer
    print('invalid input')

