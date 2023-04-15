def f1():
    print("Hey i am first function")
    a = 10
    b = 5
    x = f2(a,b)
    return x
    
def f2(x, y):
    print("I am second function")
    return x +y

sarr = [None] * (9)