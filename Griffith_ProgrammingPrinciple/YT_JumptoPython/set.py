s = set()

s1 = set([1, 2, 3])
s1

# does not allow duplicates!!
# unordered!!

s2 = set("Hello")
s2

# indexing >> turn into list or tpule
s1 = set([1, 2, 3])
l1 = list(s1)
l1
#[1, 2, 3]
l1[0]
#1
t1 = tuple(s1)
t1
#(1, 2, 3)
t1[0]
#1

# intersection, union, difference

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# intersection
s1 & s2
s1.intersection(s2)

# union
s1 | s2
s1.union(s2)

# difference
s1 - s2
s1.difference(s2)


s1 = set([1, 2, 3])
s1.add(4)
s1

s1 = set([1, 2, 3])
s1.update([4, 5, 6])
s1

s1 = set([1, 2, 3])
s1.remove(2)
s1