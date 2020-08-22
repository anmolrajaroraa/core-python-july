# def fn_name(param1, param2, ..., paramn):
#     statement1
#     statement2
#     return statement


def inputNumbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    return a, b, c, 13, 34, 5, 3, 2, 99, 33   # packing


*x, y = inputNumbers()  # unpacking
z = inputNumbers()

print("X is ", x)
print("Y is ", y)
print("Z is ", z)

# x, y = 10, 20
# x = (10, 20)
