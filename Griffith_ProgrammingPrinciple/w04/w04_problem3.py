num1 = int(input("num1: "))
num2 = int(input("num2: "))
num3 = int(input("num3: "))

# Find the maximum and minimum first
if num1 > num2:
    max = num1
    min = num2
else:
    max = num2
    min = num1

# Now place num3 correctly
if num3 > max:
    mid = max
    max = num3
elif num3 < min:
    mid = min
    min = num3
else:
    mid = num3

print(max, mid, min)