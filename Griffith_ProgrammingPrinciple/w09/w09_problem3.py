

file = input("file name: ")

try:
    with open(file, "r") as f:
        
        for line in f:
            numbers = [int(num) for num in line.split()]
            avg = sum(numbers) / len(numbers)
            print(avg)       

except:
    print("file not found")
