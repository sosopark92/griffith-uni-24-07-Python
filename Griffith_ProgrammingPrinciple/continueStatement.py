
numbers = [0, 1, 2, 3]

for n in numbers : # for n in range(4)
    if (not n):
        continue # exits body of loop, skips to next iteration
    else:
        n += 2
    print(n)