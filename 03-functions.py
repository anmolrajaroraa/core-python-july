def add():  # local variables (parameters)
    return 0


def add1(x):
    return x


def add2(x, y):
    return x + y


def add3(x, y, z):
    return x + y + z


# def addN(*numbers):   # dynamic arguments (*args)
#     sum = 0
#     for num in numbers:
#         sum += num
#     return sum

def addN(x=0, y=0, z=10, *numbers):  # default arguments
    sum = x + y + z
    for num in numbers:
        sum += num
    return sum

# normal args, default arguments, *args


# print(add2(10, 20))
# print(add1(10))
# print(add())
# print(add3(10, 20, 30))
print(addN())
