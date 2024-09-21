# Write a program that reads strings (without digits or symbols in the string) 
# typed by the user until an empty string is entered. 

# For each string, convert all words to lowercase, 
# then sort and print the words into descending order lexicographically. 


def only_str(s):
    word_list = s.lower().split()
    word_list.sort(reverse=True)
    for words in word_list:
        print(words, end=" ")
    print()

s = input("Enter a string: ")

while s != "":
      only_str(s)
      s = input("Enter a string: ")