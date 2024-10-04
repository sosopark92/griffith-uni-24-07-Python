#person.py
"""Module that defines the Person class"""

class Person:
    
    def __init__(self, name, address):
        """Creates a Person object
        
        name is of type Name
        address is of type Address
        """
        self._name = name
        self._address = address

    def __str__(self):
        """ str version of a Person object"""
        return(str(self._name) + '\n' + str(self._address))  
    
    def name(self):
        """returns the Name of the Person object"""
        return self._name
    
    def address(self):
        """returns the Address of the Person object"""
        return self._address

    def setName(self, name):
        """sets the Name of the Person object to the argument value"""
        self._name = name

    def setAddress(self, address):
        """sets the Address of the Person object to the argument value"""
        self._address = address
