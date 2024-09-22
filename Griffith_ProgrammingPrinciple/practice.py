degree = input("Enter the degrees and the unit (C/F): ")

result = ""
for c in degree:
    if c.isalnum():
        result += c
print(result)


