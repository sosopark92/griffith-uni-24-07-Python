
# opening >= 0
balance = int(input("Opening balance of account: "))

if balance < 0:
   balance = int(input("You can't open your account with less than 0 amount. Enter opening balance: "))
else:
   balance = balance

amount = int(input("Amount deposited or withdrew (negative value): "))
deposit = 0
withdraw = 0

while amount != 0:
    if amount > 0:
        deposit += amount
    else:
        withdraw += amount

    amount = int(input("Amount deposited or withdrew (negative value): "))

def summary(balance, deposit, withdraw):
    print("Opening balance:", balance)
    print("Deposits:", deposit)
    print("Withdrawals:", abs(withdraw))
    print("Closing balance:", balance + deposit + withdraw)

summary(balance, deposit, withdraw)





# while amount != 0:
#       if amount > 0:
#          deposit = balance + amount
#          withdraw = withdraw
#       if amount < 0:
#          withdraw = withdraw - amount
#          deposit = deposit
#       amount = int(input("Amount deposited or withdrew (negative value): "))



# balance = opening
# balance >= amount

#deposit
#withdraw
#balance
