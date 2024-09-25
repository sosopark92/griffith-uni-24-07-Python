

try:

    f = input("file name: ")


    with open(f, 'r') as f:
         lines = f.readlines()
         print(lines[0:2])
         print(lines[-2:])

except:
    print("file not found")



