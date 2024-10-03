#given an input number n, print a diamond shape with 2*n-1 rows.


n = int(input("Enter number: ")) #3
rows = 2*n-1
i = 1

if n >= 1:
    for i in range(i, rows, 2): #1, 3
        print(((rows-i)//2)*" ", end="")
        for j in range (0, i):
            print("x", end="")
        print()

    for k in range(rows, 0, -2): #5, 3, 1
        print(((rows-k)//2)*" ", end="")
        for s in range (0, k): 
            print("x", end="")
        print()
else:
    print()
        