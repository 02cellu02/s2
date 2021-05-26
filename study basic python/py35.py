#pb input 1234; output in words
number=input('phone:')
sum=''
dict={'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
for items in number:
    sum+=f'{dict[items]} '
    #or sum+=f'{dict.get(items,'invalid')} ' NB
print(sum)
