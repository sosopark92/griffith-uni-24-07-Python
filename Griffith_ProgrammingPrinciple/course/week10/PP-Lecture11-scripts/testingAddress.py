#testingAddress.py
#tests the code of class Address 
from address import Address

add1 = Address("1 Heights Boulevard", "any", "Pimpama", "QLD", "4209")
print(add1)
add1.updateAddress("1 Parklands drive", "", "Southport", "QLD", "4215")
print(add1)
