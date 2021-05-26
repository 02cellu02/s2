#dictionaries
customer={'name':'cel joy','age':30,"is_verify":True}
#keys should be distinct
print(customer['name'])#if invalid key,then key error
print(customer.get('birthday'))#returns none if invalid
print(customer.get('birthday','jan 1 1987'))#returns 2nd parameter if invalid key
#to edit
customer['name']='celestine'
customer["birthday"]='jan3 1994'#use can add new keys
