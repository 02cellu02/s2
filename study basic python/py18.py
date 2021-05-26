name=input("enter name: ")
if len(name)<3:
    print("name must be atleast 3 characters")
elif len(name)>50:
    print("name can be max of 50 characters")
else:
    print("looks good")
    