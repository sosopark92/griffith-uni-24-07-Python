
#ask a user for a strong
sentence = input("String? ")

#check each g, neighbour >> happy, otherwise lonely

# while sentence != "":

s = list(sentence)
count = 0
lonely = True

for i in range(0, len(s)-1):
    if (s[i] == "g") and (s[i+1] =="g"):
        lonely = False
    count += 1

print(lonely)
