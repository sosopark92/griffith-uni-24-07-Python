#testingStaff.py 
#tests the code of class Staff
from name import Name
from address import Address
from staff import Staff

name1 = Name("Dumbledore", "Albus Percival Wulfric Brian", "Mr")
address1 = Address("Hogwarts", "1 Parklands drive", "Southport", "QLD", "4215")
dumbledore = Staff(name1, address1, '1234', 'E')
print(dumbledore)
print()
name2 = Name("Snape", "Severus", "Mr")
address2 = Address("Hogwarts", "1 Parklands drive", "Southport", "QLD", "4215")
snape = Staff(name2, address2, '3456', 'E')
print(snape)

snape.addCourse("Potions101", 2024, 1)
snape.addCourse("DefenseAgainstDarkArts201", 2024, 2)
snape.addCourse("Transfiguration202", 2024, 1)
print(snape.courses())
#snape.printTeaching()

snape.removeCourse("Transfiguration202", 2024, 1)
print(snape.courses())