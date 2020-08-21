def checkPin():
    correctPIN = 1234
    PIN = int(input("Enter pin: "))
    if PIN != correctPIN:
        raise ValueError('PIN incorrect')
    return True


def checkBalance():
    balance = 10000
    amount = int(input("Enter amount to withdraw: "))
    if amount > balance:
        raise ValueError("Amount exceeds balance")
    balance -= amount
    print("Withdrawal successful ", amount)
    print("Balance leftover: ", balance)


def withdraw():
    isPINcorrect = checkPin()
    if isPINcorrect:
        checkBalance()


try:
    withdraw()
except ValueError as errorMsg:
    print(errorMsg)
except BaseException as err:
    print(err)
finally:
    print("Thanks for visiting us!")
