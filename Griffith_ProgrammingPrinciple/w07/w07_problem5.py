
opening= int(input("Opening balance of account: "))
amount = int(input("Amount deposited or withdrew (negative value): "))

def balance(opening, amount):
    deposit = 0
    withdraw = 0

    while amount != 0:       
          if amount >0:
             deposit = deposit + amount
             withdraw = withdraw
          else:
            withdraw = withdraw - amount
            deposit = deposit
          
          amount = int(input("Amount deposited or withdrew (negative value): "))

    print("Opening balance: ", opening)
    print("Deposits: ", deposit)
    print("Withdrawlas: ", withdraw)
    print("Closing balance: ", opening+deposit-withdraw)

balance(opening, amount)


    

