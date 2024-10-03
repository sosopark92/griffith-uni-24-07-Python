
s1 = input("Student 1 (courses 1-4): ")
s2 = input("Student 2 (courses 1-4): ")
s3 = input("Student 3 (courses 1-4): ")
s4 = input("Student 4 (courses 1-4): ")
s5 = input("Student 4 (courses 1-4): ")

def convert_int(list):
    list = list.split()
    int_list = []
    for i in list:
        int_list.append(int(i))
    return int_list
#def convert_int(list):
#    return [int(num) for num in input(prompt).split()]

s1 = convert_int(s1)
s2 = convert_int(s2)
s3= convert_int(s3)
s4 = convert_int(s4)
s5 = convert_int(s5)

marks = [s1, s2, s3, s4, s5]

#The highest average mark of students
avgM = [sum(s) / 4 for s in marks]
print("The highest average mark of students: ",max(avgM))

#The highest average mark of courses
avgC = []
for course_no in range(4):
    course_marks = [sMark[course_no] for sMark in marks]
    avgC.append(sum(course_marks)/5)
print("The highest average mark of courses", max(avgC))
