
def AscOrder(myList):
    """sort the list in ascending order"""

    for i in range(0, len(myList)-1):
        for j in range(i+1, len(myList)):
            #compare the elements
            if myList[i] > myList[j]:
                #swap elements
                myList[i], myList[j] = myList[j], myList[i]


n = int(input())
s = input().split()

for i in range(n):
    s[i] = int(s[i])

AscOrder(s)
print(s[0])