#pb
price=1000000
is_good_credit=True
if is_good_credit:
    down=0.1*price
else:
    down=0.2*price
print(f'down payment:${down}')