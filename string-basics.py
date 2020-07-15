Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> str1 = "Hello Everyone, this is PythOn prOgramming"
>>> str1 = 'Hello Everyone, this is PythOn prOgramming'
>>> type(str1)
<class 'str'>
>>> # string is a collection of one or more characters - character array
>>> # char arr[] = ['h', 'e', 'l', 'l', 'o']
>>> str1[0]
'H'
>>> str1[1]
'e'
>>> str1[2]
'l'
>>> str1[3]
'l'
>>> str1[4]
'o'
>>> len(str1)
42
>>> str1[42]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    str1[42]
IndexError: string index out of range
>>> str1[41]
'g'
>>> str1[40]
'n'
>>> str1[39]
'i'
>>> str1[-1]
'g'
>>> str1[-2]
'n'
>>> str1[-3]
'i'
>>> # a part of string - substring - string slicing
>>> str1[0]
'H'
>>> str1[0:10]
'Hello Ever'
>>> str1
'Hello Everyone, this is PythOn prOgramming'
>>> #  str1[ start : stop : step ]    str1[ index ]
>>> str1[ 0 : 5 ]
'Hello'
>>> str1[20]
' '
>>> str1[25]
'y'
>>> str1[24]
'P'
>>> str1[24 : 30 ]
'PythOn'
>>> str1[31:41]
'prOgrammin'
>>> str1[42]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    str1[42]
IndexError: string index out of range
>>> str1[31:42]
'prOgramming'
>>> str1[31:50]
'prOgramming'
>>> str1[50:500]
''
>>> str1
'Hello Everyone, this is PythOn prOgramming'
>>> str1[-1 : -12]
''
>>> str1[-1 : -12 : 1]
''
>>> str1[-1 : -12 : -1]
'gnimmargOrp'
>>> str1[::-1]
'gnimmargOrp nOhtyP si siht ,enoyrevE olleH'
>>> # reversing the string
>>> 'Hello Everyone, this is PythOn prOgramming.jpg'
'Hello Everyone, this is PythOn prOgramming.jpg'
>>> img = 'Hello Everyone, this is PythOn prOgramming.jpg'
>>> img[ -1 : -4 : -1 ]
'gpj'
>>> img[ -4 : -1 ]
'.jp'
>>> img[ -4 : 0 ]
''
>>> img[ -4 :  ]
'.jpg'
>>> img[ 14 : ]
', this is PythOn prOgramming.jpg'
>>> 
>>> img[20 : ]
' is PythOn prOgramming.jpg'
>>> img[0 : ]
'Hello Everyone, this is PythOn prOgramming.jpg'
>>> img[ : ]
'Hello Everyone, this is PythOn prOgramming.jpg'
>>> img
'Hello Everyone, this is PythOn prOgramming.jpg'
>>> img[ : : -1 ]
'gpj.gnimmargOrp nOhtyP si siht ,enoyrevE olleH'
>>> 
>>> str1[10 : 40: 1]
'yone, this is PythOn prOgrammi'
>>> str1[10 : 40: 2]
'yn,ti sPtO rgam'
>>> str1[10 : 40: 5]
'y  y r'
>>> str1[40 : 10: -5]
'nr y  '
>>> str1 = 'Dwayne Rock Johnson'
>>> str1
'Dwayne Rock Johnson'
>>> print(str1)
Dwayne Rock Johnson
>>> str1 = 'Dwayne 'Rock' Johnson'
SyntaxError: invalid syntax
>>> str1 = 'Dwayne "Rock" Johnson'
>>> 
