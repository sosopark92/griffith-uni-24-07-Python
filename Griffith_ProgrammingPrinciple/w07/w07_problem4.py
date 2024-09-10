#we know that th ecarpet width is 3.66m
#calculate the amount of carpet reuqired
#ask use for dimension

import math

dim1 = float(input("Enter room dmension 1 (m): "))
dim2 = float(input("Enter room dmension 2 (m): "))

while dim1 != 0 and dim1 != 0:
      #determine length and width of room
      if dim1 > dim2:
         length = dim1
         width = dim2
      else :
         length = dim2
         width = dim1
      print("Length of room = ", format(length, ".3f"), "m")
      print("Width of room = ", format(width, ".3f"), "m")

      #amount of carpet sheets
      carpet_width = 3.66

      #calculate lengthways amount of carpet required
      sheets = math.ceil(width / carpet_width) #ceil = round up
      sl = length #sl = sheet length
      cl = math.ceil(sl*sheets) #cl = carpet length

      #calculate widthways amount of carpet required
      sheets2= math.ceil(length / carpet_width) 
      sl2 = width
      cl2 = math.ceil(sl2*sheets2)

      print("Total carpet length required in lengthways manner = ", cl, "m")
      print("Total carpet length required in widthways manner = ", cl2, "m")





