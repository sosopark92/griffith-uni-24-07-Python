
#ask for file name from user
name = input("Enter the file name: ")
print("Source file name = ", name)

try:
    #open the file
    sourcefile = open(name)

    while True:
        line = sourcefile.readline()
        if not line:
            break
        print(line)

    sourcefile.close()

except:
    print("The file", name, "does not exist")
#readlines
#readline
#read


