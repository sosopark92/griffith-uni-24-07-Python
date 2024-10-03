

sentence = input("String?: ")
s = list(sentence)


lonely = True
# count = 0

for i in range(0, len(s)-1):
    if (s[i] == "g") and (s[i+1]=="g"):
        lonely = False
    # count += 1

# print("count:", count)
print("lonely:",lonely)