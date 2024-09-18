#we have a file from our stock provider what has been delivered to us after ordering from them
#we want to read in stock items from the file and update the stock count for each item

#demonstrates first part using a dict to get the unique stock items and their count

#ask for file name from user
name = input("Enter the file name: ")
print("name = ", name)
try:
    #open the file
    stockFile = open(name)
    stock = dict()  #create an empty dict

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
            item = items[1].strip(',-\'#')  #what else will you add here based on the text file?
            #item = items[1]
            if (item in stock):
                #just want to update the count
                #stock[item] += items[0]   #this is a string
                count = int(stock[item]) + int(items[0])
                #print(count)   #test
                stock[item] = count
                #print(count)
                print(item, " already in stock dict")   
            else: 
                #add a new key value pair
                stock[item] = items[0]
            print("stock = ", stock)

    stockFile.close()
        

except:
    print("The file", name, "does not exist")


    


