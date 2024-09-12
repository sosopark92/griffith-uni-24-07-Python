
while pensReq > 0 and booksReq > 0:
      if pensReq <= pens:
         pens -= pensReq
         print("Number of pens in stock: ", pens)
         if pens <= 5:
            print("There are only 5 pens or less left.")
      else:
         check = input(f"There are only {pens} pens in stock. Do you want to buy the {pens} pens? Y/N: ")
         if check == "Y":
            pens = 0
            print("New pens must be ordered")      

      if booksReq <= books:
         books -= booksReq
         print("Number of books in stock: ", books)
         if books <= 5:
            print("There are only 5 books or less left.")
      else: 
         check = input(f"There are only {books} books in stock. Do you want to buy the {books} books? Y/N: ")
         if check == "Y":
            books = 0
            print("New pens must be ordered")       
            
      pensReq = int(input("Number of pens requested by customer: "))
      booksReq = int(input("Number of books requested by customer: "))