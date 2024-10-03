#two functions
#fuction1: converts degrees in Celsius to degrees in Fahrenheit
#function2: converts degrees in Fahrenheit to degrees in Celsius
#Each function must return both values
#you can not use a list

# F = (C *1.8) + 32
# F = (C *9/5) + 32 
# C = (F - 32) * 5/9


def celcius_to_fahrenheit(celcius):
    fahrenheit = (celcius*9/5) +32
    return [celcius, fahrenheit]


degrees = celcius_to_fahrenheit(35)


print(degrees[0], "degrees Celcius", degrees[1], "degrees Fahrenheit")

