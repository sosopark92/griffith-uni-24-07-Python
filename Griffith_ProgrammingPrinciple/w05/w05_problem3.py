

# Problem3
# A palindrome is a number or a text phrase that reads the same backwards as well as forwards.
# Examples of palindromes are 123321, 1234321, 55555, 22, 454, 1, 0. 
# Write a program that reads in a positive integer number 
# and prints out whether that number is a palindrome. 



num = int(input("Enter a number: "))  # Read a positive integer from the user

if num < 0:  # Check if the number is positive
    print("Please enter a positive integer.")
else:
    original_num = num  # Store the original number for comparison
    reversed_num = 0  # Initialize the variable to store the reversed number

    # Reverse the number
    while num > 0:
        last_digit = num % 10  # Get the last digit of the current number
        reversed_num = (reversed_num * 10) + last_digit  # Append it to the reversed number
        num = num // 10  # Remove the last digit from the original number

    # Check if the original number and the reversed number are the same
    if original_num == reversed_num:
        print(original_num, "is a palindrome.")
    else:
        print(original_num, "is not a palindrome.")