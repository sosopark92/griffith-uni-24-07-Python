
s = str(input("Enter a string: "))
longest = s

while s[0] != "A":
      print(s)
      s = str(input("Enter a string: "))
      if len(s) > len(longest):
         longest = s

      if s[0] == "A":
         print(s)
         if len(s) > len(longest):
            longest = s
print("Longest was: ", longest)
  

         


    
         
