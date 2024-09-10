#problem1
    #variable, value
    #prompt the user: input()
    #how many variables? 3
    #types: float

#step1.VALUE
width = float(input("Width of the park(m): "))
length = float(input("Length of the partk(m): "))
concrete = float(input("Liters per square meter: "))

#step2. CALCULATION
#area
area = width*length #total square meters
#total amount of concrete
total_concrete = concrete*area

#step3. RESULT
print("Liters required = ", round(total_concrete, 2)) #round

