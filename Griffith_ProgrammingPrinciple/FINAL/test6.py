
filename = input("file name: ")

try:
    with open(filename, "r") as f:
         lines = f.readlines()
         for line in lines:
             line = lines.strip()
             print(line)      
                
except:
    print("file is not found")
