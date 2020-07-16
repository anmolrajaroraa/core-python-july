Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> str1 = "Dwayne Rock Johnson"
>>> print(str1)
Dwayne Rock Johnson
>>> str1 = "Dwayne "Rock" Johnson"
SyntaxError: invalid syntax
>>> str1 = "Dwayne 'Rock' Johnson"
>>> print(str1)
Dwayne 'Rock' Johnson
>>> str1 = 'Dwayne "Rock" Johnson'
>>> print(str1)
Dwayne "Rock" Johnson
>>> str1 = 'Dwayne "Rock" Johnson's in F9'
SyntaxError: invalid syntax
>>> str1 = "Dwayne "Rock" Johnson's in F9"
SyntaxError: invalid syntax
>>> str1 = "Dwayne "Rock" Johnson's in F9"
SyntaxError: invalid syntax
>>> str1 = 'Dwayne "Rock" Johnson's in F9'
SyntaxError: invalid syntax
>>> print('Dwayne "Rock" Johnson's in F9')
      
SyntaxError: invalid syntax
>>> print("Dwayne "Rock" Johnson's in F9")
SyntaxError: invalid syntax
>>> 
>>> str1 = 'Dwayne "Rock" Johnson\'s in F9'
>>> print(str1)
Dwayne "Rock" Johnson's in F9
>>> str1 = "Dwayne \"Rock\" Johnson's in F9"
>>> print(str1)
Dwayne "Rock" Johnson's in F9
>>> #    \ -> escape character (skip the next character after me)
>>> str1 = "Dwayne \"Rock\" Johnson's in F9\\"
>>> print(str1)
Dwayne "Rock" Johnson's in F9\
>>> str1 = "Dwayne \"Rock\" Johnson's in F9\"
SyntaxError: EOL while scanning string literal
>>> #  \n   ->  new line character
>>> str1 = "Dwayne \"Rock\" Johnson's in F\n9"
>>> print(str1)
Dwayne "Rock" Johnson's in F
9
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> str1 = 'hello jenny. whats going on with Dwayne Rock Johnson'
>>> str1.capitalize()
'Hello jenny. whats going on with dwayne rock johnson'
>>> str1.title()
'Hello Jenny. Whats Going On With Dwayne Rock Johnson'
>>> str1.center()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    str1.center()
TypeError: center() takes at least 1 argument (0 given)
>>> str1.center(50)
'hello jenny. whats going on with Dwayne Rock Johnson'
>>> str1.center(80)
'              hello jenny. whats going on with Dwayne Rock Johnson              '
>>> str1.center(90)
'                   hello jenny. whats going on with Dwayne Rock Johnson                   '
>>> str1.center(100)
'                        hello jenny. whats going on with Dwayne Rock Johnson                        '
>>> str1.center(110)
'                             hello jenny. whats going on with Dwayne Rock Johnson                             '
>>> str1.center(110)
'                             hello jenny. whats going on with Dwayne Rock Johnson                             '
>>> str1.center(150)
'                                                 hello jenny. whats going on with Dwayne Rock Johnson                                                 '
>>> str1.center(250)
'                                                                                                   hello jenny. whats going on with Dwayne Rock Johnson                                                                                                   '
>>> str1.center(100)
'                        hello jenny. whats going on with Dwayne Rock Johnson                        '
>>> str1.center(100, '$')
'$$$$$$$$$$$$$$$$$$$$$$$$hello jenny. whats going on with Dwayne Rock Johnson$$$$$$$$$$$$$$$$$$$$$$$$'
>>> str1.center(90, '$')
'$$$$$$$$$$$$$$$$$$$hello jenny. whats going on with Dwayne Rock Johnson$$$$$$$$$$$$$$$$$$$'
>>> str1.count('o')
6
>>> str1.count('on')
2
>>> str1.count('hello')
1
>>> str1.count('O')
0
>>> str1.count('Hello')
0
>>> str1.count('dwayne')
0
>>> str1.count('Dwayne')
1
>>> str1
'hello jenny. whats going on with Dwayne Rock Johnson'
>>> str1.count('o')
6
>>> str1.find('o')
4
>>> str1[4]
'o'
>>> str1.find('o')
4
>>> str1.find('o', 5)
20
>>> str1.find('o', 21)
25
>>> str1.find('o', 26)
41
>>> str1.find('o', 42)
46
>>> str1.find('o', 47)
50
>>> str1.find('o', 51)
-1
>>> str1.find('O')
-1
>>> str1.index('o')
4
>>> str1.index('O')
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    str1.index('O')
ValueError: substring not found
>>> str1
'hello jenny. whats going on with Dwayne Rock Johnson'
>>> str1.endswith('on')
True
>>> str1.endswith('Johnson')
True
>>> str1.endswith('johnson')
False
>>> str1.startswith('hello')
True
>>> str1.startswith('hello python')
False
>>> str2 = "abhja788abna"
>>> str2.isalpha()
False
>>> str2.isalnum()
True
>>> str1.isalpha()
False
>>> "hello jenny".isalpha()
False
>>> "hellojenny".isalpha()
True
>>> "hellojenny123".isalpha()
False
>>> "hellojenny123".isalnum()
True
>>> "hellojenny123$".isalnum()
False
>>> "hellojenny123 ".isalnum()
False
>>> "hellojenny123 ".isnumeric()
False
>>> "hellojenny123".isnumeric()
False
>>> "123".isnumeric()
True
>>> #int, float, str, boolean
>>> a = 10
>>> a = a + 1
>>> a
11
>>> a = 10
>>> id(a)
4564143568
>>> a = a + 1
>>> a
11
>>> id(a)
4564143600
>>> str1
'hello jenny. whats going on with Dwayne Rock Johnson'
>>> str1[0] = 'H'
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    str1[0] = 'H'
TypeError: 'str' object does not support item assignment
>>> del str1[0]
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    del str1[0]
TypeError: 'str' object doesn't support item deletion
>>> str1.lower()
'hello jenny. whats going on with dwayne rock johnson'
>>> str1.upper()
'HELLO JENNY. WHATS GOING ON WITH DWAYNE ROCK JOHNSON'
>>> str1.split()
['hello', 'jenny.', 'whats', 'going', 'on', 'with', 'Dwayne', 'Rock', 'Johnson']
>>> "hello jenny".split()
['hello', 'jenny']
>>> "hello jenny".split()
['hello', 'jenny']
>>> "hellojenny".split()
['hellojenny']
>>> words = str1.split()
>>> words
['hello', 'jenny.', 'whats', 'going', 'on', 'with', 'Dwayne', 'Rock', 'Johnson']
>>> type(words)
<class 'list'>
>>> # list = array
>>> words.join(' ')
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    words.join(' ')
AttributeError: 'list' object has no attribute 'join'
>>> ' '.join(words)
'hello jenny. whats going on with Dwayne Rock Johnson'
>>> '*'.join(words)
'hello*jenny.*whats*going*on*with*Dwayne*Rock*Johnson'
>>> '*****'.join(words)
'hello*****jenny.*****whats*****going*****on*****with*****Dwayne*****Rock*****Johnson'
>>> str1.split()
['hello', 'jenny.', 'whats', 'going', 'on', 'with', 'Dwayne', 'Rock', 'Johnson']
>>> str1
'hello jenny. whats going on with Dwayne Rock Johnson'
>>> str1.split('o')
['hell', ' jenny. whats g', 'ing ', 'n with Dwayne R', 'ck J', 'hns', 'n']
>>> str1.split('D')
['hello jenny. whats going on with ', 'wayne Rock Johnson']
>>> str1.split('Dwayne')
['hello jenny. whats going on with ', ' Rock Johnson']
>>> 
