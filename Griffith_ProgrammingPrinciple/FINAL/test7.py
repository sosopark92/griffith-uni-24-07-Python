
stock = {"socks":[5, 2]}

def ordered (item_name, stock):
    total_ordered = stock[item_name][1]
    return total_ordered

def additem (item_name, num_stock, stock):
    stock[item_name] = [int(num_stock), 0]
    return stock

print(additem("pants", 5, stock))

def orderItem(item_name, quantity, stock):
    if item_name in stock:
        available_stock, total_ordered = stock[item_name]

        if quantity <= available_stock:
            # Update stock and total ordered
            stock[item_name][0] -= quantity  # Reduce available stock
            stock[item_name][1] += quantity  # Increase total ordered
            print(quantity, item_name, "ordered.")
        else:
            print("Insufficient stock. Only", available_stock, item_name, "available.")
    else:
        print(item_name, "is not in stock.")

orderItem("socks", 3, stock)
print(stock)    

