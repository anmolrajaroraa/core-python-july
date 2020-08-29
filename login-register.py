import csv
# comma separated values

print('''
1. Login
2. Register
''')

choice = int(input("Enter choice: "))

# if choice == 1:
#     isLoginSuccessful = False
#     usernameOrEmail = input("Enter username/email: ")
#     password = input("Enter password: ")
#     with open("users.csv") as fileStream:
#         reader = csv.reader(fileStream)
#         for row in reader:
#             if usernameOrEmail == row[0] or usernameOrEmail == row[2]:
#                 if password == row[3]:
#                     print("Login successful!")
#                     isLoginSuccessful = True
#                     break
#     if not isLoginSuccessful:
#         print("Login failed")

if choice == 1:
    usernameOrEmail = input("Enter username/email: ")
    password = input("Enter password: ")
    with open("users.csv") as fileStream:
        reader = csv.reader(fileStream)
        for row in reader:
            if usernameOrEmail == row[0] or usernameOrEmail == row[2]:
                if password == row[3]:
                    print("Login successful!")
                    break
        else:
            print("Login failed!")

# for-else block
# else says now I'm a follower of for block
# if 'for' loop ends gracefully, else will run
# but if we break the for loop(terminate it abruptly) then else is also terminated hence 'else' block will not run

elif choice == 2:
    emailExists = False
    username = input("Enter username: ")
    fullname = input("Enter fullname: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    # fileStream = open("users.csv", "w")
    # fileStream.close()

    with open("users.csv") as fileStream:
        reader = csv.reader(fileStream)
        for row in reader:
            # print(row)
            emailFromDB = row[2]
            if email == emailFromDB:
                print("Email already registered..please login")
                emailExists = True
                break

    if not emailExists:
        with open("users.csv", "a", newline='') as fileStream:
            writer = csv.writer(fileStream)
            writer.writerow([username, fullname, email, password])
        print("Registered successfully...")
