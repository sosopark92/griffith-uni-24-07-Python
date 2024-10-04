#address.py
"""Module that defines class Address"""

class Address:
    #constructor
    """Creates an instance of Address
    line 1 is the first line of the address
    line 2 is the second line of the address
    state is the state
    postalCode is the postal code """
    def __init__(self, line1, line2, suburb, state, postalCode):
        self._line1 = line1
        self._line2 = line2
        self._suburb = suburb
        self._state = state
        self._postalCode = postalCode

    #define how to convert an Address object to a str
    def __str__(self):
        return self.address()
    
    #returns the address
    def address(self):
        a = ""
        if self._line1 != '':
            a += self._line1 + ', '
        if self._line2 != '':
            a += self._line2 + ', '
        a += self._suburb + ', ' + self._state + ', ' + self._postalCode
        return a
    
    #changes/updates the address
    def updateAddress(self, line1, line2, suburb, state, postalCode):
        self._line1 = line1
        self._line2 = line2
        self._suburb = suburb
        self._state = state
        self._postalCode = postalCode