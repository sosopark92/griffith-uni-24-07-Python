# Write a program that allows the user to enter the marks of multiple students,
# for each student the marks for up to 5 courses
# the number of distinctions obtained per student 
# (assume distinction refers to a grade greater or equal to 75)
# the number of distinctions and failures per course

#enter the marks of multiple students
s1 = input("Enter marks: ")
s2 = input("Enter marks: ")
s3 = input("Enter marks: ")
s4 = input("Enter marks: ")
s5 = input("Enter marks: ")

#marks into integer
def int_list(s):
    return [int(n) for n in s.split()]


mark1 = int_list(s1)
mark2 = int_list(s2)
mark3 = int_list(s3)
mark4 = int_list(s4)
mark5 = int_list(s5)

# the number of distinctions obtained per student 
def s_distinction(mark):
    return len([d for d in mark if d >= 75])

#course marks
# marks = [s1, s2]
marks = [s1, s2, s3, s4, s5]

marks = [d.split() for d in marks]


#list of marks by course
course_mark_list = []
for course_no in range(5):
    course_marks = [sMark[course_no] for sMark in marks]
    course_marks = [int(n) for n in course_marks]
    course_mark_list.append(course_marks)


for course_no in range(5):
    count = 0 
    for d in course_mark_list[course_no]:
        if d >= 75:
           count += 1
        else: continue
    print("distinction: ", count, "failure: ", 5-count)
           










# print("student1: ", s_distinction(mark1))
# print("student2: ", s_distinction(mark2))
# print("student3: ", s_distinction(mark3))
# print("student4: ", s_distinction(mark4))
# print("student5: ", s_distinction(mark5))
   

# mark1 = [int(n) for n in s1.split()]

# mark2 = s2.split()
# mark3 = s3.split()
# mark4 = s4.split()
# mark5 = s5.split()

# def celcius_to_fahrenheit(celcius):
#       fahrenheit = (celcius*9/5) +32
#       return (celcius, fahrenheit)


# degrees = celcius_to_fahrenheit(35)


# print(degrees[0], "degrees Celcius", degrees[1], "degrees Fahrenheit")

