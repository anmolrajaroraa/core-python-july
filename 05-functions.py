def inputNumbers():
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    return a, b


def calc(operator):
    x, y = inputNumbers()
    print(eval(x + operator + y))  # concatenation  -> 10 + 20


print('''
1. Add
2. Sub
3. Mul
4. Div
''')

choice = int(input("Enter your choice: "))

operations = {
    1: '+',
    2: '-',
    3: '*',
    4: '/'
}
# operations[choice]()
operator = operations.get(choice)
calc(operator)

# "1 + 2"
