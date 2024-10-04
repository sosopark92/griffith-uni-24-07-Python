#testingName.py
#tests the code of class Name
from name import Name

name1 = Name("Potter", "Harry", "Mr")
name2 = Name("Granger", "Hermione", "Miss", famNameFirst=True)
name3 = Name("Dumbledore", "Albus Percival Wulfric Brian", "Prof")

print(name1.familyName())
print(name3.otherNames())
print(name1)
print(name2)
name2.setFamilyName("Weasley")
print(name2)
print(type(name2))

