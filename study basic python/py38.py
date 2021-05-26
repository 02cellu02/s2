#convert emojis in string using fn
def convert_emoji(string):
    sum=''
    str=string.split(' ')
    dic={':(':'😔',':)':'😃'}
    for ch in str:
        sum+=f'{dic.get(ch,ch)} '
    return sum


string=input('<')
print(convert_emoji(string))
