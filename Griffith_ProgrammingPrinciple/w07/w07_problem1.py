# Problem: Write a program that prompts for and reads strings 
# until a string that starts with the letter “A” is entered (inclusive), 
# then prints the longest string that was entered. 

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
  

         


    
         
