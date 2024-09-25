

file = input("file name: ")

try:
    with open(file, "r") as f:

        avg_list = []

        for line in f:
            numbers = [int(num) for num in line.split()]
            avg = sum(numbers) / len(numbers)
            print("avrage of line: ", avg)
            avg_list.append(avg)
        print("min: ", min(avg_list))
        print("max: ", min(avg_list))
            

except:
    print("file not found")
