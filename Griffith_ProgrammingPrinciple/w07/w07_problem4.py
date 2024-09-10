#we know that th ecarpet width is 3.66m
#calculate the amount of carpet reuqired
#ask use for dimension

import math

dim1 = float(input("Enter room dmension 1 (m): "))
dim2 = float(input("Enter room dmension 2 (m): "))

#determine length and width of room
if dim1 > dim2:
   length = dim1
   width = dim2
else :
   length = dim2
   width = dim1

#calculate lengthways amount of carpet required
carpet_width = 3.66

#width: amount of carpet sheets
sheets = math.ceil(width / cw) #ceil = round up
sl = math.ceil(length) #sl = sheet length
cl = sheets*sl #cl = carpet length

#calculate widthways amount of carpet required
sheets2 = math.ceil(length / cw) 
sl2 = math.ceil(width) 
cl2 = sheets*sl 

