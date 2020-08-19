# try block means try to run this code
# if it contains any exception then hand over that exception
# to except block
# except block handles runtime errors (exceptions)
# we can have multiple except blocks
# each block is dedicated for handling a specific type of exception like ValuError, IndexError
# if exception doesn't matches with any except block
# then the last block having BaseException consumes each exception and prints out th error message as required
# finally block - always execute code will go here
# file close, database connetion closing, user thanku msg
while True:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        q = num1 / num2
        print("Quotient is ", q)

        list1 = [1, 2, 3, 4, 5]
        # print(list1[100])

        file = open('patterns.py')
        print(file.read())
        file.close()
        break
    except ValueError:
        print("Only integers are allowed...")
    except ZeroDivisionError:
        print("Please don't enter 0 for num2")
    except IndexError as error:
        print("Some error occured...", error)
    except BaseException as error:
        print("Some error occured...", error)
    finally:
        print("Finally ran...")
        if file != None:
            file.close()
        # while True:
        #     numberValid = True
        #     num1 = input("Enter first number: ")
        #     for digit in num1:
        #         if ord(digit) >= 48 and ord(digit) <= 57:
        #             continue
        #         else:
        #             print("Number not valid")
        #             numberValid = False
        #             break
        #     if numberValid:
        #         break
        # num2 = int(input("Enter second number: "))
