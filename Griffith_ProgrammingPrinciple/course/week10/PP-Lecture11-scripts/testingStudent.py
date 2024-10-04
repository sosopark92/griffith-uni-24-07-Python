#testingStudent.py
#tests the code of class Student
from name import Name
from address import Address
from student import Student

name1 = Name("Potter", "Harry", "Mr")
name2 = Name("Dumbledore", "Albus Percival Wulfric Brian", "Prof")

address1 = Address("Cupboard under the stairs", "Pivet Drive", "Southport", "QLD", "4215")
address2 = Address("Griffith University", "1 Parklands drive", "Southport", "QLD", "4215")

harry = Student(name1, address1, "12345")
#print(harry)
#print(harry.id())
harry.setName("Dobey")
#print(harry.name())

harry.addCourse("Potions101")
harry.addCourse("MagicalCreatures101")
harry.updateGrade("Potions101", 75)
harry.addCourse("DefenseAgainstDarkArts101")
harry.addCourse("Botany101")
harry.addCourse("Transfiguration101")
harry.updateGrade("Botany101", 30)
#print(harry.courses())
harry.removeCourse("Potions101")
harry.removeCourse("Potions102")
#print(harry.courses())
harry.printReportCard()