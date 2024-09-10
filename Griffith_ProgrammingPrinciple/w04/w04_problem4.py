base_wage = 36.25
base_hour = 37
bonus = 200

total_hours = float(input("how many hours were worked? "))
total_car = int(input("Total number of car sold? "))

salary = base_wage*total_hours

# Calculate salary based on hours worked
if total_hours > 36:
    salary = base_wage*base_hour + 1.5*base_wage*(total_hours-base_hour)
else:
    salary
    
# Add bonus if more than 5 cars were sold
if total_car > 5:
    salary = salary + bonus*(total_car-5)

print(salary)

