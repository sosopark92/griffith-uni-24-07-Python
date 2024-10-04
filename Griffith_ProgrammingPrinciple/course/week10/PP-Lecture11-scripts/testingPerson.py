#testingPerson.py
#tests the code of class Person 
from name import Name
from address import Address
from person import Person

name1 = Name("Potter", "Harry", "Mr")
name2 = Name("Dumbledore", "Albus Percival Wulfric Brian", "Prof")

address1 = Address("Cupboard under the stairs", "Pivet Drive", "Southport", "QLD", "4215")
address2 = Address("Griffith University", "1 Parklands drive", "Southport", "QLD", "4215")

harry = Person(name1, address1)
dumbledore = Person(name2, address2)

print(harry)
print(dumbledore)

