

black = int(input("Number of black pens in stock: "))
blue = int(input("Number of blue pens in stock: "))
red = int(input("Number of red pens in stock: "))
a4 = int(input("Number of A4 books in stock: "))
a5 = int(input("Number of A5 books in stock: "))

stock = {'black': black, 'blue': blue, 'red': red, 'A4': a4, 'A5': a5}

pens = int("Number of pens requested by customer: ")
books = 1 #first deal with pens and then go to books
otherPens = 'yes'

#can use other stopping conditions that make sense
while (pens > 0) or (books > 0): # why not 'and'?
      #first deal with pens
      while otherPens.lower() != "no":
            colour = input("Colour of pens: ")
            if colour.lower() in stock.key():
            #print(stock[col])
                if pens <= stock[colour]: #enough pens in stock
                   stock[colour] -= pens
                else:
                   buy = input("There are only" + str(stock[colour]) + "pens in stock.")
                   if buy.upper() == "Y":
                       stock[colour] = 0 #bought all the pens
            #can add here a else and manage a wrong colour
            #code eto manage wrong colour

            otherPens = input("Any other pens? ")


            #secondly deal with the books

            otherBooks = "yes"
            
