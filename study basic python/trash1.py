def print_rangoli(size):
    # your code goes here
    a='abcdefghijklmnopqrstuvwxyz'
    li=[('-'.join([a[size-i-1] for i in range(j+1)]+[a[size-i-1] for i in range(j+1)][-2::-1])).center((size-1)*4+1,'-') for j in range(size) ]
    nli=('\n'.join(li))
    print(f"{nli}\n{(nli[-2::-1])}")
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)