#sort list in descending order

def descOrder(myList):
    """sort the list in descending order"""

    for i in range(0, len(myList)-1):
        for j in range(i+1, len(myList)):
            #compare the elements
            if myList[j] > myList[i]: #myList[j] < myList[i] -- ascending
                #swap elements
                myList[i], myList[j] = myList[j], myList[i]

l = [20, 2, 4, 5]

descOrder(l)
print(l)