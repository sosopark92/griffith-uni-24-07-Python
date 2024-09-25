


# enter the marks of multiple students
# for each student the marks for up to 5 courses

s1 = input("Enter marks: ")
s2 = input("Enter marks: ")

#marks into integer
def int_list(s):
    return [int(n) for n in s.split()]

mark1 = int_list(s1)
mark2 = int_list(s2)

# the number of distinctions obtained per student 
def s_distinction(mark):
    return len([d for d in mark if d >= 75])

print("the number of distinctions obtained s1: ", s_distinction(mark1))
print("the number of distinctions obtained s2: ", s_distinction(mark2))

#student course marks
marks = [mark1, mark2]

#The number of distinctions and failures per course
distinction = []
failure = []
dcount = 0
fcount = 0
for student_no in range(2):
    for course_no in range(2):
        if marks[student_no][course_no] >= 75:
           dcount += 1
           distinction.append(dcount)
        else:
           fcount += 1
           failure.append(fcount) 
    print(distinction, failure)
