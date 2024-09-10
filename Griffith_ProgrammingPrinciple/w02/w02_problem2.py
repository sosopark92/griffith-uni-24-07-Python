#problem1
    #variable, value
    #prompt the user: input()
    #how many variables? 
    #types: float, int

#step1.VALUE
hours = float(input("Number of hours worked per day: "))
days = int(input("Number of days worked in a week: "))
annual_salary = float(input("Annual salary: "))

#step2. CALCULATION
#work hours
work_hours = hours*days*52
#hourly_wage
hourly_wage = annual_salary/work_hours

#step3. RESULT
#round
print("hourly_wage: ", round(hourly_wage,2))


