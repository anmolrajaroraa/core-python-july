# def square(num):
#     return num * num
#     # print() # unreachable code


# # number = 849493
# # print(f"Square of {number} is {square(number)}")

numbers = list(range(1, 100))
# square_of_numbers = []
# for number in numbers:
#     # sq = square(number)
#     # print(f"Square of {number} is {sq}")
#     square_of_numbers.append(square(number))

# print(square_of_numbers)

# list1 = list(map(square, numbers))
# print(list1)


# def divisibleBy3(number):
#     return number % 3 == 0


# list2 = list(filter(divisibleBy3, numbers))
# print(list2)

# numbersThatAreDivisibleBy3 = []

# for number in numbers:
#     if divisibleBy3(number):
#         numbersThatAreDivisibleBy3.append(number)

# print(numbersThatAreDivisibleBy3)

list3 = list(filter(lambda num: num % 3 == 0, numbers))
'''
1. fn creation
2. list creation
3. loop on numbers
4. call lambda fn (anonymous fn or lambda expression)
5. check if returned value is true or not
6. if true then store number in list
'''
print(list3)

list4 = list(map(lambda num: num * num, numbers))
print(list4)
