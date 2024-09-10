

#stock of books and pens
pen =  int(input("Number of pens in stock: "))
book =  int(input("Number of books in stock: "))

#customer buys
penReq: int(input("Number of pens requested by customer: "))
bookReq: int(input("Number of books requested by customer: "))

#def
while penReq > 0 and bookReq > 0:
#check the stock and if not enough ask question
      if penReq <= pen:
#update stock
         pens -= penReq #remove from stock the requested pens
         print("Number of pens in stock:", pen)
      else:
#check whether we need to order new stock
        buyOrnot = input("There are only", pens, "in stock. Do you want to buy the", pens, "? Y/N")
        if byOrnot == "Y" :
           pens = 0
           print("New pens must be ordered")


#ask again for input
penReq: int(input("Number of pens requested by customer: "))
bookReq: int(input("Number of books requested by customer: "))
