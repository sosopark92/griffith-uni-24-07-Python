# Problem: Given starting and ending years, 
# write a program with a function to calculate the number of days 
# from the starting year to ending year inclusive.  
# Hints: Write a function to check for a leap year. 
# Type Bool and Boolean Expressions. 


# 1y = 365d / 366d
# Leap year

def days(year):
    if year % 4 == 0:
       return 366
    else:
       return 365

y1 = int(input())
y2 = int(input())

s = 0
for i in range(y1, y2+1):
    s = s + days(i)
print(s)
