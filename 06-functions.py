x = 100


def outer():
    # x = 200
    global x
    x = x + 100
    print("Outer fn called..", x)

    def inner():
        print("Inner fn called")

    # inner()

    print("Outer fn going to finish")

    return inner


result = outer()
print("Result:", result)
result()
# result()
# outer.inner()
