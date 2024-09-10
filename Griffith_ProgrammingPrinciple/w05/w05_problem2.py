# Problem: The grades at a university are awarded based on the marks awarded for the course out
# of 100. Marks of 85 or above receive the grade of 7. Marks less than 85 but that are 75 or above
# receive the grade of 6. Marks less than 75 but that are 65 or above receive the grade of 5. Marks
# less than 65 but that are 50 or above receive the grade of 4. Anything less than 50 gets the grade
# of F. Write a program that asks the user to enter their marks, calculates the grade and prints the
# grade awarded. When the user finished entering their marks, the average mark and average grade
# are printed to the console.

mark = int(input("Enter a mark: "))
sumM = 0 #sum of marks
sumG = 0 #sum of grades
count = 0
avgM = 0
avgG = 0

# calculation
while mark >= 0 :
      count =+ 1
      sumM += mark
      sumG += mark
      if    mark >= 85 :
            grade = 7
            print("Grade is", grade)
      elif  75 <= mark < 85 :
            grade = 6
            print("Grade is", grade)
      elif  65 <= mark < 75 :
            grade = 5
            print("Grade is", grade)
      elif  50 <= mark < 65 :
            grade = 4
            print("Grade is", grade)
      else:
            grade = "F"
            print("Grade is", grade)
      mark = int(input("Enter a mark: "))
if count != 0 :
   avgM = sumM / (count+1)
   avgG = sumG / (count+1)

print("Avrage mark: ", avgM)
print("Average grade: ", avgG)