#Fibonacci

n = int(input("Enter a number: "))
f1 = 0
f2 = 1

if (n > 1):
    print("0 1", end=" ")
elif (n == 1):
    print("0")


for i in range(3, n+1):
    sum = f1 + f2
    if (i % 4 != 0):
        print(sum, end=" ")
    else :
        print(sum)
    #update vales
    f1 = f2
    f2 = sum
