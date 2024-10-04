#staff.py
"""Module that defines the Person class"""

from person import Person

class Staff(Person):
    
    def __init__(self, name, address, id, level):
        """Creates a Staff object
    
        name is of type Name
        address is of type Address
        id is of type str
        level is A/B/C/D/E"""
        Person.__init__(self, name, address)
        self._id = id
        self._level = level
        if level=='D':
            self._name.setTitle('A/Prof')
        elif level=='E':
            self._name.setTitle('Prof')
        self._teaching = dict()

    #defines how to convert a Staff object to a str
    def __str__(self):
        a = super().__str__()
        a = str(a) + ", " + self._id
        return(a)
    
    #returns the id
    def id(self):
        return self._id
    
    #add a course that the Staff object teaches
    def addCourse(self, courseCode, year, trimester):
        """Add a course that the Staff object teaches to the _teaching dictionary
        courseCode is the code of the course
        year is the year that the course is taught
        trimester is the trimester that the course is taught
        """
        k = str(year) + "-T" + str(trimester)
        if k not in self._teaching.keys():
           self._teaching[k] = [courseCode]
        else:
            self._teaching[k].append(courseCode)

    def removeCourse(self, courseCode, year, trimester):
        """Removes a course from a Staff object"""
        k = str(year) + "-T" + str(trimester)
        if k in self._teaching.keys():
            c = self._teaching[k]
            c.remove(courseCode)
            self._teaching[k] = c

    #get method
    def courses(self):
        """Returns a dictionary of all of the courses that the Staff object taught"""
        return self._teaching
    
    def printTeaching(self):
        """Prints for each year-trimester all courses that the Staff object taught"""
        print(self._name)
            
        for tri in self._teaching.keys():
            print(tri, end=": ")
            for course in self._teaching[tri]:
                print(course, end=' ')
            print()
    