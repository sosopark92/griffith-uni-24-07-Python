count = 0
sumM = 0
sumG = 0

mark = int(input("Enter a mark (negative to stop): "))

while mark >= 0:
    count += 1
    if mark >= 85:
        grade = 7
    elif 75 <= mark < 85:
        grade = 6
    elif 65 <= mark < 75:
        grade = 5
    elif 50 <= mark < 65:
        grade = 4
    else:
        grade = 0  # 'F' will be treated as grade 0

    sumM += mark
    sumG += grade

    print("Grade is", grade if grade > 0 else 'F')

    mark = int(input("Enter a mark (negative to stop): "))

if count > 0:
    print("Average mark: ", sumM / count)
    print("Average grade: ", sumG / count)
else:
    print("No valid marks entered.")
