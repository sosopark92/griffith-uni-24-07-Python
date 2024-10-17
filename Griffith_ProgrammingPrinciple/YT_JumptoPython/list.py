#list is mutable

odd = []
type(odd)

odd = [1, 3, 5, 7, 9]
odd

a = [] # a = list()
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

b[0]+b[2]

e[-1][0]

b + c #[1, 2, 3, 'Life', 'is', 'too', 'short']
b * 3 #[1, 2, 3, 1, 2, 3, 1, 2, 3]

# len()
len(b) #3

# type error
b[1] + c[0] #error
str(b[1]) + c[0]

# update
num = [1, 2, 3]
num[2] = 4
num

# del object
num = [1, 2, 3]
del num[0:1]
num

# append()
num = [1, 2, 3]
num.append(4)
num.append([5, 6])
num.append((7, 8))
num.append("hi")
num

# sort()
order = [1, 5, 3]
order.sort() #alphabetical order 
order

# reverse()
opposite = [2, 6, 1] #Reverse the current list as it is.
opposite.reverse()
opposite

# index()
point = [2, 3, 4]
point.index(2) #0
point.index(3) #1

# insert(a, b)
num = [1, 2, 3, 4]
num.insert(0, 5)
num

# remove(x) "removes the first occurrence of x from the list."
t = [1, 2, 3, 1, 2, 3]
t.remove(3)
t

# pop() "returns the last element of the list and removes it"
t = [1, 2, 3]
t.pop()
t

t = [1, 2, 3]
t.pop(1)
t

# count()
a = [1, 2, 3, 1]
a.count(1)

