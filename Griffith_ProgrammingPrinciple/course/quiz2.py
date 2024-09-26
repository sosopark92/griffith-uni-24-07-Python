

# Read a poem from a text file and output the following statistics about the poem:

# How many words does the longest line in the poem have? len()
# Are all lines in the poem unique, i.e. the line occurs only once in the poem? set()
# Are all words in the poem unique, i.e. each word occurs only once in the poem? split(), set()

#ask for file name from user
file = input("Enter the file name: ")
print("file = ", file)

try:
    #open and close the file
    with open(file, 'r') as poem: 

        longest_line_words = 0
        unique_lines = set()
        unique_words = set()
        non_unique_lines = False

        for line in poem:
            # Strip unnecessary characters and spaces
            line = line.strip(',-\'#\" \n .')
            # Split the line into words
            words = line.split()

            # Check the length of the longest line: max(), len()
            longest_line_words = max(longest_line_words, len(words))

            # Check if the line is unique: set()
            if line in unique_lines:
               non_unique_lines = True
               unique_lines.add(line)

             # Check if the words in lines are unique: set()
            for word in words:
                unique_words.add(word)
        
        print("How many words does the longest line in the poem have? ", longest_line_words)
        if not non_unique_lines:
            print("All lines are unique.")
        else:
            print("There are duplicate lines.")
        print("Number of unique words:", len(unique_words))
        print(line)

except:
    print("file not found.")


    # if not line:
    #             break
    #         else:
    #             line_count += 1