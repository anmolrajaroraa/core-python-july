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

def addN(x, y, z=10, *numbers):  # default arguments
    sum = x + y + z
    for num in numbers:
        sum += num
    return sum

# normal args, default arguments, *args


# print(add2(10, 20))
# print(add1(10))
# print(add())
# print(add3(10, 20, 30))
print(addN(99, 88))

# keyword arguments


def printEmployeeDetails(id, name, salary="Not known", designation="To be decided", department="To be provided later", city="Address not known", **otherDetails):
    print("Id is", id)
    print("Name is", name)
    print("Salary is", salary)
    print("Designation is", designation)
    print("Department is", department)
    print("City is", city)
    print("Other Details: ", otherDetails)


# printEmployeeDetails(101, "Ram", 15000, "Manual Tester",
#                      "Testing", "Delhi", 2000, 3000, 4000, 2500, 15000)

printEmployeeDetails(102, "Shyam")

printEmployeeDetails(101, "Ram", city="Delhi", designation="Manual Tester",
                     department="Testing", salary=15000, HRA=2000, DA=3000, TA=4000, PF=2500, tax=15000)

printEmployeeDetails(101, "Ram", department="Testing", salary=15000, HRA=2000,
                     DA=3000, TA=4000, PF=2500, tax=15000, city="Delhi", designation="Manual Tester")


'''
while calling - positional arguments, keyword args, whichever key is not found, all those key value are pushed in **kwargs (extra keyword arguments)
positional arguments should always come before default arguments
in parameter list, *args should always be the last argument
otherwise it will consume all the values coming in and other parameters will starve
overriding - if you create two or more fns with same name then the fn written at the last will be the active fn and the others will become inactive
'''
