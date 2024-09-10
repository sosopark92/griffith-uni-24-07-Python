#define function with local scope
def f(x):
    
    print("b x=", x) 

    x += 1
    print("c x=", x)


#define global scope
y = 1
print("a y=", y)
f(y)
print("d y=", y)