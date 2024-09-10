#changing grade example using for loop

#determine how grades will be entered
gradeNumber = int(input("How many grades will be entered? "))
total = 0 #sum of the grades

#using the for loop
for i in range(gradeNumber):
    grade = float(input("Enter a grade: "))
    if (grade >= 0) :
        total += grade
    else: 
        gradeNumber -= 1
        
print("Number of grades: ", gradeNumber)
print("Grade average: ", (total/gradeNumber))

