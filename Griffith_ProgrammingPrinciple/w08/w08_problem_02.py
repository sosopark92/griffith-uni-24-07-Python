

# Enter two lists of integers

def int_list(list):
    list = list.split()
    int_list = []
    for n in list:
        int_list.append(int(n))
    return int_list

# Calculate the sum of the first and the last integers in each list
def list_sum(list):
    if len(list) == 1:
       return list[0]
    else:
       return list[0]+list[-1]

#list1, list2
list1 = input("list1: ")
list2 = input("list2: ")

list1 = int_list(list1)
list2 = int_list(list2)

sum_1 = list_sum(list1)
sum_2 = list_sum(list2)

# Print the larger sum
# Print Same when they are tie
if sum_1 > sum_2:
    print(sum_1)
elif sum_1 < sum_2:
    print(sum_2)
else:
    print("tie")
    
