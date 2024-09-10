# Problem_1
# Write a program that reads whole numbers entered by the user 
# until a zero is entered, 
# and then prints the number of positive numbers that were entered. 



count = 0
number = int(input("Enter a number: "))

while number != 0 :
      if number > 0 :
         count += 1
      number = int(input("Enter a number: "))

print(count, "positive numbers were entered.")

