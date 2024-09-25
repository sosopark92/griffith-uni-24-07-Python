file = input("Enter file name: ")
char_count = 0
word_count = 0
line_count = 0

try:    
    with open(file, 'r') as f:  
         for line in f:
            char_count += len(line)
            word_count += len(line.split())
            line_count += 1
         print(char_count)
         print(word_count)
         print(line_count)

except:
    print("file not found")




    