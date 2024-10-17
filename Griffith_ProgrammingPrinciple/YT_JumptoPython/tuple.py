# tuple is immutable
# indexing, slicing is available

t1 = ()
t2 = (1,) # when there is only one element, a comma (,) must be added after the element.
t3 = (1, 2, 3)
t4 = 1, 2, 3 # parenthesis () can be omitted
t5 = ('a', 'b', ('ab', 'cd'))

t1 = (1, 2, 'a', 'b')
t1[0]
t1[1:3]

t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
t3 = t1 + t2
t3

t2 = (3, 4)
t3 = t2 * 3
t3

t1 = (1, 2, 2, 'a', 'b')
t1[0:2:]

l1 = [1, 2, 'a']
len(l1)