x = 100  # global variables
y = 200


def inputNumbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    return None  # packing


def add(x, y):   # local variables (parameters)
    return x + y


def add2():
    return x + y


def add3():
    sum = 0
    numbers = inputNumbers()
    if not numbers:
        return 0
    if type(numbers) == int:
        return numbers
    for num in numbers:
        sum += num
    return sum


print(add(10, 20))
print(add2())
print(add3())
