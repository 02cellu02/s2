n=int(input())
l=[]
flag=True
for i in range(n):
    flag=True
    l.append(input())
    if l[i][0]=='4' or l[i][0]=='5' or l[i][0]=='6':
        if (len(l[i])-l[i].count('-'))==16:
            if l[i].isdigit():
                x=1
                y=1
                z=0
                while x<len(l[i]):
                    if x!='-':
                        if y==4:                                
                            print('invalid')
                            flag=False
                            break
                        if l[i][x]==l[i][z]:
                            y+=1
                        else:
                            y=1
                            z=x
                    x+=1
                if flag:
                    print('valid')
            else:
                c=1
                for k in l[i]:
                    if c%5==0:
                        if k!='-':
                            print('invalid1')
                            flag=False
                            break
                    else:
                        if not k.isdigit():
                            print('invalid2')
                            flag=False
                            break
                    c+=1
                if flag==True:
                    x=1
                    y=1
                    z=0
                    while x<len(l[i]):
                        if l[i][x]!='-':
                            if y==4:
                                print('invalid')
                                flag=False
                                break
                            if l[i][x]==l[i][z]:
                                y+=1
                            else:
                                y=1
                                z=x
                        x+=1
                    if flag:
                        print('valid')
        else:
            print('invalid3')
    else:
        print('invalid4')