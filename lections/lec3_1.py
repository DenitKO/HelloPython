def calc1(x):
    return x+10
# print(calc1(10))


def calc2(x):
    return x*10
# print(calc2(10))


def math(op, x):
    print(op(x))


# math(calc1, 10)
# math(calc2, 10)


# def sum(x, y):
#     return x+y
# эта лямбда, тоже самое что и фунция выше
sum = lambda x, y: x+y

def mylt(x, y):
    return x*y


def calc(op, a, b):
    print(op(a, b))
    return op(a, b)
 
calc(lambda x, y: x+y, 4, 5) # можно использовать лямбду напрямую, вместо аргумента