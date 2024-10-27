
filename = input("file name: ")

try:
    with open(filename, "r") as f:
            lines = f.readlines()

            totals = {}

            for line in lines:
                line = line.strip().split(" ")
                labels = line[0]
                numbers = line[1:]

                total = sum(float(num) for num in numbers) if numbers else 0.0
                total = round(total, 2)

                totals[labels] = total

                print(labels, totals[labels])

    highest_label = list(totals.keys())[0]
    lowest_label = list(totals.keys())[0]
    highest_total = totals[highest_label]
    lowest_total = totals[lowest_label]

    for label, total in totals.items():
        if total > highest_total:
            highest_total = total
            highest_label = label
        if total < lowest_total:
            lowest_total = total
            lowest_label = label
            
    print("Highest total:", highest_label)
    print("Lowest total:", lowest_label)       
                     
except:
    print("file is not found")
