#pillandrom

number = int(input("Enter a positive number: "))
original_num = number
reversed_num = 0

#reverse the number
#n = 12321
while number > 0:
    last_digit = number % 10
    reversed_num = reversed_num * 10 + last_digit
    number = number // 10

if original_num == reversed_num:
    print(original_num, "is a pillandrom.")
else:
    print(original_num, "is not a pillandrom.")