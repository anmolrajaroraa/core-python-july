Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 1 + 2
3
>>> print
<built-in function print>
>>> print()   paranthesis
SyntaxError: invalid syntax
>>> 
>>> comments
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    comments
NameError: name 'comments' is not defined
>>> 
>>> # svknslvksnklsnbslkbn
>>> # this is a note (single line comment)
>>> 
>>> # print() -> () paranthesis
>>> print()

>>> # print() ->by default it gives us a new line
>>> print(" My nane is Ram ")
 My nane is Ram 
>>> print(" My name is Ram ")
 My name is Ram 
>>> print("Hello, world")
Hello, world
>>> a = 10   # dynamically typed
>>> b = 20
>>> print("a")
a
>>> print(a)
10
>>> print(b)
20
>>> c = a + b
>>> print(c)
30
>>> print("Sum of a and b is c")
Sum of a and b is c
>>> print("C is c")
C is c
>>> print("C is", c)
C is 30
>>> print(" Sum of ", a, "and", b, "is", c)
 Sum of  10 and 20 is 30
>>> print("C is %d" %a)
C is 10
>>> print(" Sum of %d and %d is %d " %a,b,c )
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(" Sum of %d and %d is %d " %a,b,c )
TypeError: not enough arguments for format string
>>> print(" Sum of %d and %d is %d " %(a,b,c) )    # (a,b,c) -> tuple -> array
 Sum of 10 and 20 is 30 
>>> print(" Sum of %d and %d is %d " %(a,b, "thirty" ) )
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print(" Sum of %d and %d is %d " %(a,b, "thirty" ) )
TypeError: %d format: a number is required, not str
>>> 
>>> 
>>> print("Sum of {} and {} is {}".format(a,b,c) )
Sum of 10 and 20 is 30
>>> print("Sum of {} and {} is {}".format(a,b,"thirty") )
Sum of 10 and 20 is thirty
>>> print("Sum of {} and {} is {}".format(a,b, True) )
Sum of 10 and 20 is True
>>> print("Sum of {} and {} is {}".format(a,b, a+b ) )
Sum of 10 and 20 is 30
>>> print("Sum of {} and {} is {}".format(a,b, d=
				      ) )
SyntaxError: invalid syntax
>>> print("Sum of {} and {} is {}".format(a,b, d=a+b ) )
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print("Sum of {} and {} is {}".format(a,b, d=a+b ) )
IndexError: tuple index out of range
>>> 
>>> 
>>> d
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    d
NameError: name 'd' is not defined
>>> 
>>> 
>>> # walrus operator
>>> print("Sum of {} and {} is {}".format(a,b, d:=a+b ) )
SyntaxError: invalid syntax
>>> print("Sum of {} and {} is {}".format(a,b, d=a+b ) )
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print("Sum of {} and {} is {}".format(a,b, d=a+b ) )
IndexError: tuple index out of range
>>> print("Sum of {} and {} is {}".format(a,b, a+b ) )
Sum of 10 and 20 is 30
>>> 
>>> print("Sum of {} and {} is {}, Diff btw {} and {} is {}, Product of {} and {} is {}, Quotient of {} and {} is {}".format(a,b, a+b, a,b, a-b, a,b, a*b, a,b, a/b ) )
Sum of 10 and 20 is 30, Diff btw 10 and 20 is -10, Product of 10 and 20 is 200, Quotient of 10 and 20 is 0.5
>>> print(" Sum of {} and {} is {},\n Diff btw {} and {} is {},\n Product of {} and {} is {},\n Quotient of {} and {} is {}".format(a,b, a+b, a,b, a-b, a,b, a*b, a,b, a/b ) )
 Sum of 10 and 20 is 30,
 Diff btw 10 and 20 is -10,
 Product of 10 and 20 is 200,
 Quotient of 10 and 20 is 0.5
>>> print(" Sum of {} and {} is {},\n Diff btw {} and {} is {},\n Product of {} and {} is {},\n Quotient of {} and {} is {}".format(a,b, a+b, a-b, a*b, a/b) )
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    print(" Sum of {} and {} is {},\n Diff btw {} and {} is {},\n Product of {} and {} is {},\n Quotient of {} and {} is {}".format(a,b, a+b, a-b, a*b, a/b) )
IndexError: tuple index out of range
>>> print(" Sum of {0} and {1} is {2},\n Diff btw {0} and {1} is {3},\n Product of {0} and {1} is {4},\n Quotient of {0} and {1} is {5}".format(a,b, a+b, a-b, a*b, a/b) )
 Sum of 10 and 20 is 30,
 Diff btw 10 and 20 is -10,
 Product of 10 and 20 is 200,
 Quotient of 10 and 20 is 0.5
>>> 
>>> print(" Sum of a and b is a+b,\n Diff btw {0} and {1} is {3},\n Product of {0} and {1} is {4},\n Quotient of {0} and {1} is {5}")
 Sum of a and b is a+b,
 Diff btw {0} and {1} is {3},
 Product of {0} and {1} is {4},
 Quotient of {0} and {1} is {5}
>>> print(" Sum of {a} and {b} is {a+b},\n Diff btw {0} and {1} is {3},\n Product of {0} and {1} is {4},\n Quotient of {0} and {1} is {5}")
 Sum of {a} and {b} is {a+b},
 Diff btw {0} and {1} is {3},
 Product of {0} and {1} is {4},
 Quotient of {0} and {1} is {5}
>>> print(f" Sum of {a} and {b} is {a+b},\n Diff btw {0} and {1} is {3},\n Product of {0} and {1} is {4},\n Quotient of {0} and {1} is {5}")
 Sum of 10 and 20 is 30,
 Diff btw 0 and 1 is 3,
 Product of 0 and 1 is 4,
 Quotient of 0 and 1 is 5
>>> 
>>> print(f" Sum of {a} and {b} is {a+b},\n Diff btw {a} and {b} is {a-b},\n Product of {a} and {b} is {a*b},\n Quotient of {a} and {b} is {a/b}")
 Sum of 10 and 20 is 30,
 Diff btw 10 and 20 is -10,
 Product of 10 and 20 is 200,
 Quotient of 10 and 20 is 0.5
>>> 
>>> print(f" Sum of {a=} and {b} is {a+b},\n Diff btw {a} and {b} is {a-b},\n Product of {a} and {b} is {a*b},\n Quotient of {a} and {b} is {a/b}")
SyntaxError: invalid syntax
>>> 
>>> print('''
ajjcana,nalv
svsbsbsbs
sbsbsb
bsb
sbbsbsb
''')

ajjcana,nalv
svsbsbsbs
sbsbsb
bsb
sbbsbsb

>>> print(f"""
 Sum of {a} and {b} is {a+b}
 Diff btw {a} and {b} is {a-b}
 Product of {a} and {b} is {a*b}
 Quotient of {a} and {b} is {a/b}""") #text block

 Sum of 10 and 20 is 30
 Diff btw 10 and 20 is -10
 Product of 10 and 20 is 200
 Quotient of 10 and 20 is 0.5
>>> print(f"""Result is:
 Sum of {a} and {b} is {a+b}
 Diff btw {a} and {b} is {a-b}
 Product of {a} and {b} is {a*b}
 Quotient of {a} and {b} is {a/b}""") #text block
Result is:
 Sum of 10 and 20 is 30
 Diff btw 10 and 20 is -10
 Product of 10 and 20 is 200
 Quotient of 10 and 20 is 0.5
>>> # f-string -> fast, formatting
>>> #Type "help", "copyright", "credits" or "license" for more information.
>>> a = 10
>>> b = 20
>>> print("Sum of {} and {} is {}".format(a,b, d = a+b))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: Replacement index 2 out of range for positional args tuple
>>> print("Sum of {} and {} is {}".format(a,b, d := a+b))
Sum of 10 and 20 is 30
>>> d
30
>>> print(f"Sum of {a} and {b} is {a+b}")
Sum of 10 and 20 is 30
>>> print(f"Sum of {a=} and {b=} is {a+b=}")
Sum of a=10 and b=20 is a+b=30
>>> 
