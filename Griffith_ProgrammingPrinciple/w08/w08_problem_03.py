
#ask a user for a strong
sentence = input("String? ")

#check each g, neighbour >> happy, otherwise lonely

# while sentence != "":

count = 0
lonely = True

for i in range(0, len(sentence)-1):
    if (sentence[i] == "g") and (sentence[i+1] =="g"):
        lonely = False
    count += 1

print(lonely)
