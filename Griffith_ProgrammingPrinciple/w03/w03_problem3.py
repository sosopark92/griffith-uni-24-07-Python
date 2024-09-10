#variables
big_hall = int(input("How many big exam halls?: "))
small_hall = int(input("How many small exam halls?: "))

#calculation
school_class = (45*big_hall + 22*small_hall)//25 

#result
print("Number of classes: ", school_class)
