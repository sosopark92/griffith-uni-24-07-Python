a = "hobby"
print(a.count('b')) 
print(a.count('b')) #index()
print(a.count('x')) #-1

b = ', '.join('abcd')
print(b)

c = ', '.join(['a','b','c','d'])
print(c)

a = "hi"
print(a.upper())
a = "HI"
print(a.lower())

a = "  hi"
a.lstrip() #delete left space

a = "hi  "
a.rstrip() #delete right space

a = "  hi  "
a.strip()

a = "Life is too short."
a.replace("Life", "Your hair")
a.split()

b = "a:b:c:d"
b.split(":")
