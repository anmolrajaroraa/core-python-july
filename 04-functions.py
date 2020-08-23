def inputNumbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    return a, b


def add():
    x, y = inputNumbers()
    print(x + y)


def sub():
    x, y = inputNumbers()
    print(x - y)


def mul():
    x, y = inputNumbers()
    print(x * y)


def div():
    x, y = inputNumbers()
    print(x / y)


def errorHandler():
    print("Invalid choice")


print('''
1. Add
2. Sub
3. Mul
4. Div
''')

choice = int(input("Enter your choice: "))

operations = {
    1: add,
    2: sub,
    3: mul,
    4: div
}
# operations[choice]()
operations.get(choice, errorHandler)()

# operations = [add, sub, mul, div]
# choice -= 1
# operations[choice]()

# if choice == 1:
#     add()
# elif choice == 2:
#     sub()
# elif choice == 3:
#     mul()
# else:
#     div()

'''
def first():
...     return 10 + 20
... 
>>> def second():
...     return 20 - 10
... 
>>> operations = [first(), second()]
>>> operations
[30, 10]
>>> operations = [first, second]
>>> operations
[<function first at 0x1080738c8>, <function second at 0x108073950>]
>>> operations[0]
<function first at 0x1080738c8>
>>> operations[0]()
30
>>> operations[1]()
10
'''
