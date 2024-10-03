#two functions
#fuction1: converts degrees in Celsius to degrees in Fahrenheit
#function2: converts degrees in Fahrenheit to degrees in Celsius
#Each function must return both values
#you can not use a list

# F = (C *1.8) + 32
# F = (C *9/5) + 32 
# C = (F - 32) * 5/9


degree = input("Enter the degrees and the unit (C/F): ")

d = ""
for c in degree:
    if c.isalnum():
        d += c
print(d)


def Convert_FtoC(d):
    d = float(d[:d.find("F")])       
    c = round((d - 32) * 5/9, 2)
    print(d,"F is ",c,"C")

def Convert_CtoF(d):
    d = float(d[:d.find("C")])
    f = round((d * 1.8) + 32, 2)
    print(d,"C is ",f,"F")


if d.endswith("F"):
   Convert_FtoC(d)
else:
   Convert_CtoF(d)


