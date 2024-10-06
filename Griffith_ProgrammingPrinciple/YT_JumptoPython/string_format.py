#f string format
name = "Harry"
age = 20
a = f"My name is {name} and I am {age+1}."
print(a)

number = 3.141592
y = f"The number is {number:0.4f}"
print(y)

number = 1000000
t = f"{number:,}"
print(t)