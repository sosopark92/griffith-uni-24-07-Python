#we have a file from our stock provider what has been delivered to us after ordering from them
#we want to read in stock items from the file and update the stock count for each item

#ask for file name from user
name = input("Enter the file name: ")
print("name = ", name)
try:
    #open the file
    stockFile = open(name)
    stock = []

    #read in all items from file
    for line in stockFile:
        #processing the data        
        #want to split the line
        items = line.split()
        print("new item = ", items)
        #want to add item to stock if it is not there yet, otherwise update the number of items
                
        if (len(items) == 2):       
            items[0] = int(items[0])
            if (len(stock) == 0):
                stock.append(items)
                print(stock)
            else:
                stock.sort()
                print("sorted stock:", stock)
                found = False
                for elements in stock:
                    if (elements[1]==items[1]):
                        elements[0] += items[0]
                        found = True
                if (not found):
                    stock.append(items)
    
    stockFile.close()

except:
    print("The file", name, "does not exist")


    