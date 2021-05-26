#pb
prev='stop'
inst=input('<').lower()
while inst!='quit':
    if inst=='help':
        print('start-to start the car')
        print('stop-to stop the car')
        print('quit-to exit')
    elif inst=='start':
        if prev==inst:
            print('hey, the car has already started')
        else:
            print('car started ...ready to go!')
    elif inst=='stop':
        if prev==inst:
            print('hey the car has already stopped')
        else:
            print('car stopped.')
    else:
        print("i don't understand this")
    prev=inst
    inst=input('<').lower()
    