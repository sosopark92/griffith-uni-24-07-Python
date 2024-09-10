base_price = float(input("base price: "))
weight = float(input("weight: "))
distance = float(input("distance: "))

if distance < 250:
    discount = 0
elif distance < 500:
    discount = 0.1
elif distance < 1000:
    discount = 0.15
elif distance < 2000:
    discount = 0.2
elif distance < 3000:
    discount = 0.35
else :
    discount = 0.50

shipping_cost = base_price * weight * distance * (1-discount)

print("shipping_cost: ",shipping_cost)


