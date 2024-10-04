#student.py
"""module that defines the Student Class"""

from person import Person

class Student(Person):
    """Creates a Student object
    
    name is of type Name
    address is of type Address
    id is of type str"""
    def __init__(self, name, address, id):
        #super().__init__(name, address)  #calls super class's init method
        Person.__init__(self, name, address)
        self._id = id
        self._courses = dict()

    def __str__(self):
        """defines how to convert a Student object to str"""
        a = super().__str__() #calls super class's __str__ method
        a = str(a) + ", " + self._id
        return a
        
    def id(self):
        """"returns the student ID"""
        return self._id
    
    def addCourse(self, courseCode, grade=-1):
        """adds a course to a Student object's dict _courses
        courseCode is the key
        grade is the associated value"""
        self._courses[courseCode] = grade

    def updateGrade(self, courseCode, grade):
        """updates the grade of the specific course"""
        if courseCode in self._courses:
            self._courses[courseCode] = grade

    def removeCourse(self, courseCode):
        """Removes a specific course from _courses"""
        if courseCode in self._courses:
            del self._courses[courseCode]
            return True
        else:
            return False
        
    def courses(self):
        """returns the dict containing all courses and their associated grades"""
        return self._courses
    
    def printReportCard(self):
        """prints the report card of the Student object"""
        print(self._name)
        for course in self._courses.keys():
            print(course, ":", self._courses[course])
    
    
    
    
