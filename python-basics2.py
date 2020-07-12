Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = input("Enter your name: ")
Enter your name: Ram
>>> name
'Ram'
>>> print(f"Welcome {name}")
Welcome Ram
>>> print(f"Welcome {fullname := input("Enter your name: ")}")
SyntaxError: invalid syntax
>>> print(f"Welcome {fullname := input('Enter your name: ')}")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(f"Welcome {fullname := input('Enter your name: ')}")
NameError: name 'fullname' is not defined
>>> # single-line comment
>>> # if triple quotes syntax is used within print() it is treated as text block which will get printed
>>> # but if triple quotes syntax is used without print then it is treated as multi-line comment
>>> '''
print(f' Welcome { (fullname := input("Enter your name: " ) ) } to PythonWorld ')
Enter your name: Ram Kumar Sharma
 Welcome Ram Kumar Sharma to PythonWorld 
>>> fullname := input("Enter your name: " )
  File "<stdin>", line 1
    fullname := input("Enter your name: " )
             ^
SyntaxError: invalid syntax
>>> fullname = input("Enter your name: " )
Enter your name: Ram Kumar SHARMA
>>> print(f'Welcome {fullname} to PythonWorld')
Welcome Ram Kumar SHARMA to PythonWorld'''
'\nprint(f\' Welcome { (fullname := input("Enter your name: " ) ) } to PythonWorld \')\nEnter your name: Ram Kumar Sharma\n Welcome Ram Kumar Sharma to PythonWorld \n>>> fullname := input("Enter your name: " )\n  File "<stdin>", line 1\n    fullname := input("Enter your name: " )\n             ^\nSyntaxError: invalid syntax\n>>> fullname = input("Enter your name: " )\nEnter your name: Ram Kumar SHARMA\n>>> print(f\'Welcome {fullname} to PythonWorld\')\nWelcome Ram Kumar SHARMA to PythonWorld'
>>> 
>>> first_number = input("Enter first number: ")
Enter first number: 10
>>> second_number = input("Enter second number: ")
Enter second number: 20
>>> print(f"Sum of f_num and s_num is {first_number + second_number}")
Sum of f_num and s_num is 1020
>>> print(f"Sum of f_num and s_num is {first_number - second_number}")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(f"Sum of f_num and s_num is {first_number - second_number}")
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> # input() always gives us strings
>>> 
>>> first_number = int( input("Enter first number: ") )
Enter first number: 10
>>> second_number = int( input("Enter second number: ") )
Enter second number: 20
>>> print(f"Sum of f_num and s_num is {first_number - second_number}")
Sum of f_num and s_num is -10
>>> print(f"Sum of f_num and s_num is {first_number + second_number}")
Sum of f_num and s_num is 30
>>> first_number = input("Enter first number: ")
Enter first number: 189293839
>>> type( first_number )
<class 'str'>
>>> first_number = intinput("Enter first number: ")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    first_number = intinput("Enter first number: ")
NameError: name 'intinput' is not defined
(
>>> first_number = int( input("Enter first number: ") )
Enter first number: 34535252
>>> type( first_number )
<class 'int'>
>>> 
>>> # binary number - 0 and 1
>>> # octal - 0 to 7
>>> # decimal - 0 to 9
>>> # hexadecimal - 0 to 9, A, B, C, D, E, F
>>> 
>>> a = 99
>>> bin(a)
'0b1100011'
>>> b = 1100011
>>> type(b)
<class 'int'>
>>> b = 0b1100011
>>> type(b)
<class 'int'>
>>> int( b )
99
>>> int( 1100011 )
1100011
>>> int( 0b1100011 )
99
>>> int( 0o1100011 )
294921
>>> int( 0x1100011 )
17825809
>>> 
>>> a = 99
>>> oct(a)
'0o143'
>>> hex(a)
'0x63'
>>> int(0x63)
99
>>> int(0o143)
99
>>> 1 + 2
3
>>> 1 - 2
-1
>>> 1 * 2
2
>>> 1 / 2
0.5
>>> 1 % 2
1
>>> 53635 / 433
123.86836027713626
>>> type(123.86836027713626)
<class 'float'>
>>> round(123.86)
124
>>> round(123.36)
123
>>> 53635 // 433
123
>>> #  / -> classic division
>>> #  // -> floor division
>>> 
>>> a = 10
>>> b = 20
>>> print(f"
      
SyntaxError: EOL while scanning string literal
>>> print(f"Sum of {a} and {b} is {a+b}\nDiff btw {a} and {b} is {a-b}\nProduct of {a} and {b} is {a*b}\nQuotient of {a} and {b} is {a/b}")
Sum of 10 and 20 is 30
Diff btw 10 and 20 is -10
Product of 10 and 20 is 200
Quotient of 10 and 20 is 0.5
>>> print(f'''Result is:
Sum of      -> {a} and {b} is {a+b}
Diff btw    -> {a} and {b} is {a-b}
Product of  -> {a} and {b} is {a*b}
Quotient of -> {a} and {b} is {a/b}
''')
Result is:
Sum of      -> 10 and 20 is 30
Diff btw    -> 10 and 20 is -10
Product of  -> 10 and 20 is 200
Quotient of -> 10 and 20 is 0.5

>>> """
print(f'''Result is:
... Sum of      -> {a} and {b} is { (sum := a+b)}
... Diff btw    -> {a} and {b} is { (diff := a-b) }
... Product of  -> {a} and {b} is { (prod := a*b) }
... Quotient of -> {a} and {b} is { (q := a/b) }
... ''')
Result is:
Sum of      -> 10 and 20 is 30
Diff btw    -> 10 and 20 is -10
Product of  -> 10 and 20 is 200
Quotient of -> 10 and 20 is 0.5
>>> sum
30
>>> diff
-10""")
SyntaxError: invalid syntax
>>> 
>>> #   ** -> for calculating powers
>>> pow(10,5)
100000
>>> 10 ** 5
100000
>>> 10 * 5
50
>>> pow(2,8)
256
>>> 2 ** 18
262144
>>> 
