
# for i in range(25, -1, 5): #range(start, end, increase)
#     print(i, end=" ")
# print()

#prompt user for number of rows and columns
# rows = int(input("Number of rows: "))
# columns = int(input("Number of columns: "))

# #what will we use here as sequence?
# # for c in range(columns): #why start with 1?
# #     print("#",end=" ")

# for r in range(rows):
#     for c in range(columns):
#         print("#", end="")
#     print()

userString = input("Enter a string: ")

num = 0
for s in userString:
    if(type(s) == "int"):
        num += 1
print("Number of digits in string, ", userString, ":", num)