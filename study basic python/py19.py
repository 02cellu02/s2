#problem
weight=int(input('Weight: '))
unit=input('(L)bs or (k)g: ').upper()
if unit=='K':
    print(f'u r {weight*20/9}')
else:
    print((f'u r {weight*9/20}'))
    