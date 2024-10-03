sentence = input("String?: ")

count = 0
lonely = True

for i in sentence:
    if (count+1 == len(sentence)):
        break
    if (i == "g") and (sentence[count+1] == "g"):
        lonely = False  
    count += 1
print(lonely)


# sentence = input("String?: ")

# count = 0
# lonely = True


# for i in range(0, len(sentence-1)):
#     if sentence[i] == "g" and sentence[i+1]=="g":
#         lonely = False
#         count += 1
# print(lonely)    