
# Problem: Write a program to manage the inventory of a store for books and pens. 
# A customer can buy a combination of books and pens, 
# but you cannot sell them items that are not in stock. 
# When there are only 5 books or pens left, 
# you need to provide a message that new stock must be ordered and for which item. 
# If a customer buys items or stock has been ordered, 
# you must update the quantity of each item accordingly.


pens =  int(input("Number of pens in stock: "))
books =  int(input("Number of books in stock: "))

pensReq = int(input("Number of pens requested by customer: "))
booksReq = int(input("Number of books requested by customer: "))

while pensReq > 0 and booksReq > 0:
      if pensReq <= pens:
         pens -= pensReq
         print("Number of pens in stock: ", pens)
         if pens <= 5:
            print("There are only 5 pens or less left.")
      
      if booksReq <= books:
         books -= booksReq
         print("Number of books in stock: ", books)
         if books <= 5:
            print("There are only 5 books or less left.")

      pensReq = int(input("Number of pens requested by customer: "))
      booksReq = int(input("Number of books requested by customer: "))


      

# while pensReq > 0 and booksReq > 0:
#       if pensReq <= pens:
#          pens -= pensReq
#          print("Number of pens in stock: ", pens)
#          if pens <= 5:
#             print("There are only 5 pens or less left.")
#       else:
#          check = input(f"There are only {pens} pens in stock. Do you want to buy the {pens} pens? Y/N: ")
#          if check == "Y":
#             pens = 0
#             print("New pens must be ordered")      

#       if booksReq <= books:
#          books -= booksReq
#          print("Number of books in stock: ", books)
#          if books <= 5:
#             print("There are only 5 books or less left.")
#       else: 
#          check = input(f"There are only {books} books in stock. Do you want to buy the {books} books? Y/N: ")
#          if check == "Y":
#             books = 0
#             print("New pens must be ordered")       
            
#       pensReq = int(input("Number of pens requested by customer: "))
#       booksReq = int(input("Number of books requested by customer: "))