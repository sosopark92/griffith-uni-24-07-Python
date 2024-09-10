# fruit = input("Favourite fruit: ")
# portions = int(input("How many fruit or vegetable portions did you eat today? "))

# if (portions < 5):
#     print("You should try to eat some more fruit or veggies today. Since you love, ", fruit, "how about eating some more",fruit, set="-")
# else:
#     print("Your are eating enough fruit and veggies!", end=" ")
#     print("Keep it up!")
# print("Fruit and veggies are good for you!")

cost = float(input("Cost of items: "))
discount = 0
revisedCost = cost * (1 - discount)

if 0 <= cost < 100:
    discount = 0
    print("You do not qualify yet! You still need to add something to your cart to the value of $100.")
elif 100 <= cost < 200:
    discount = 0.05
    print("You qualify for a 5% discount!")
elif 200 <= cost < 250:
    discount = 0.1
    print("You qualify for a 10% discount!")
else:
    discount = 0.15
    print("You qualify for a 15% discount!")


print("The new discounted cost of your items is", revisedCost)