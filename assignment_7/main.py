
def get_disscount(n):
    discounts = {1:[range(10,20), .2], 2:[range(20, 50), .3], 3:[range(50, 100), .4]}
    if n < 10:
        return 1
    elif n >= 100:
        return .5
    else:
        for key, value in discounts.items():
            if n in value[0]:
                return value[1]
            
def get_order(price):
    order = int(input("Number of units to order: "))
    return round((price * order) - ((price * order) * get_disscount(order)), 2)

print(get_order(99))