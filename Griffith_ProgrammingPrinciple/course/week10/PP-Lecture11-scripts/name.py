#file name.py
"""A module that defines class Name"""

class Name:
    
    #constructor
    """Creates an instance of class Name
    familyName is the family name/surname
    otherNames is the first and middle names
    title is the title
    famNameFirst indicates whether the family name should be first or not"""
    def __init__(self, familyName, otherNames, title, famNameFirst=False):
        self._familyName = familyName
        self._otherNames = otherNames
        self._title = title
        self._famNameFirst = famNameFirst

    #modify how the Name instance is converted to a str
    def __str__(self):
        #print("here is Name's str method")
        if self._famNameFirst:
            #want to first do family name, then other names
            return(self._title + " " + self._familyName + " " + self._otherNames)
        else:
            #want to first do other names, then family name
            return(self._title + " " + self._otherNames + " " + self._familyName)

    #get functions to allow access to the attribute's value

    #returns the family name/surname
    def familyName(self):
        return self._familyName
    
    #returns the first name and middle names
    def otherNames(self):
        return self._otherNames
    
    #returns the title
    def title(self):
        return self._title
    
    #returns whether the family name should be first or not
    def famNameFirst(self):
        return self._famNameFirst

    #set functions to change an attribute's value
    def setFamilyName(self, fn):
        self._familyName = fn

    def setOtherNames(self, on):
        self._otherNames = on

    def setTitle(self, t):
        self._title = t

    def setFamNameFirst(self, fnf):
        self._famNameFirst = fnf

