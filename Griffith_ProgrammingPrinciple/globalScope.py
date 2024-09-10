#define function with local scope
def f():
    x = 2

    print("a. x=", x)
    print("a. y=", y) #global variable

#define global scope
y = 1
f()
print("c. y=", y)