
stock = {"socks":[5, 2]}

def ordered (item_name, stock):
    total_ordered = stock[item_name][1]
    return total_ordered

print(ordered("socks", stock))


def additem (item_name, num_stock, stock):
    stock[item_name] = [int(num_stock), 0]
    return stock

print(additem("pants", 5, stock))
