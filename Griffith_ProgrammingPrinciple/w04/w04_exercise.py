# print("you win if you guess the magic number.")
# num=int(input("guess the number: "))
# if(num==7):
#     print("Congrats!")
#     print("You won")
# else:
#     print("Wrong number.")
#     print("Thank you for playing!")

#whileLoop1
#print the numbers 1 to 10 on one line

# i = 1 #initialisation is first time we give value
# while i <= 10:
#     print(i, end = " ") #space after value, not new line
#     i = i + 1 #increment i
# print() #adding a newline after all values are printed

# #whileLoop3
# #changing magic number example using while loop
# CorrectNumber = 7
# #getting first number from user
# num = int(input("Enter a number: "))
# #when should we stop the while loop?
# while num !=7:
#     #print message to user, hint for next guess
#     if num < 7:
#         print("Incorrect guess. Number is too small!")
#     else: #why only 1 alternative here are not 2?
#         print("Incorrect guess. Number is too large!")
#         #get next number from user
#     num = int(input("Try again! Enter a number: "))
# print("Correct! Lucky number 7!")

#averageGrade
#sentinel pattern

grade = float(input("Enter a grade(negative value to stop): "))
sum = 0
count = 0

while grade > 0:
    sum += grade
    count += 1
if  count != 0:
    avg = sum / count+1
else: 
    grade = float(input("Enter a grade(negative value to stop): ")) 