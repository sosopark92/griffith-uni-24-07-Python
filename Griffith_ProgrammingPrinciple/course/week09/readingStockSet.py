#we have a file from our stock provider what has been delivered to us after ordering from them
#we want to read in stock items from the file and update the stock count for each item

#ask for file name from user
name = input("Enter the file name: ")
print("name = ", name)
try:
    #open the file
    stockFile = open(name)
    stock = set()  #create an empty set

    #read in all items from file
    for line in stockFile:
        #processing the data        
        #want to split the line
        items = line.split()
        print("line = ", items)
        #want to add item to stock if it is not there yet, otherwise update the number of items
                
        #add just the item name to the set
        if (len(items) == 2):    
            #remove unwanted characters from item name
            item = items[1].strip(',-\'#')
            if (items[1] in stock):
                print("item already in stock set")   
            stock.add(item)
            print("stock = ", stock)
    
    stockFile.close()

except:
    print("The file", name, "does not exist")


    


