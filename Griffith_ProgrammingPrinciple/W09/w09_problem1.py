

try:

    f1 = input("source file name: ")
    f2 = "empty_to_fill.txt"

    with open(f1, 'r') as f1, open(f2, 'w') as f2:

        empty_lines = 0

        for line in f1:
            if not line.strip() == "":
                f2.write(line)
            else:
                empty_lines += 1
        print(empty_lines)

except:
    print("file not found")



