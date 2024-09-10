

s = str(input("Input a string? "))


def is_digit(s):
    i = '_'
    new_str = ''

    for k in s:
        if k.isdigit():
           new_str += i
        else:
           new_str += k
    print(new_str)

while s.isdigit() == False:   
      is_digit(s)

      if s.isdigit() == True:
         is_digit(s)
      s = str(input("Input a string? "))


# while s.isdigit() == False:   
#       i = '_'
#       new_str = ''

#       for k in s:
#           if k.isdigit():
#              new_str += i
#           else:
#              new_str += k
#       print(new_str)

#       if s.isdigit() == True:
#          i = '_'
#          new_str = ''

#          for k in s:
#              if k.isdigit():
#                 new_str += i
#              else:
#                 new_str += k
#          print(new_str)
#       s = str(input("Input a string? "))
