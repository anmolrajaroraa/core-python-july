Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # int, float, string, boolean, byte, complex
>>> a = 10
>>> type(a)
<class 'int'>
>>> a = 10.5
>>> type(a)
<class 'float'>
>>> a = "ten"
>>> type(a)
<class 'str'>
>>> a = True
>>> type(a)
<class 'bool'>
>>> a = true
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a = true
NameError: name 'true' is not defined
>>> a = "True"
>>> type(a)
<class 'str'>
>>> # ascii table and unicode table
>>> # c language -> 1 byte of memory is consumed by 1 character
>>> name = "Ram"
>>> name = "राम"
>>> name
'राम'
>>> name.encode()
b'\xe0\xa4\xb0\xe0\xa4\xbe\xe0\xa4\xae'
>>> x = 'र'
>>> int(x)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    int(x)
ValueError: invalid literal for int() with base 10: 'र'
>>> ord('र')
2352
>>> ord('ा')
2366
>>> ord('म')
2350
>>> chr(2350)
'म'
>>> chr(2366)
'ा'
>>> chr(2352)
'र'
>>> chr(2351)
'य'
>>> '\xe0\xa4\xb0'.decode()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    '\xe0\xa4\xb0'.decode()
AttributeError: 'str' object has no attribute 'decode'
>>> b'\xe0\xa4\xb0'.decode()
'र'
>>> #  encode() is used with string to see the actual bytes which are stored instead of foreign characters   (str -> byte)
>>> x = 'abc'
>>> type(x)
<class 'str'>
>>> x = b'abc'
>>> type(x)
<class 'bytes'>
>>> b'abc'.decode()
'abc'
>>> b'abc\xa0'.decode()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    b'abc\xa0'.decode()
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa0 in position 3: invalid start byte
>>> b'abc\xe0'.decode()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    b'abc\xe0'.decode()
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe0 in position 3: unexpected end of data
>>> ord('₹')
8377
>>> chr(8377)
'₹'
>>> chr(8378)
'₺'
>>> chr(8376)
'₸'
>>> '₹'.encode()
b'\xe2\x82\xb9'
>>> b'I have \xe2\x82\xb910'.decode()
'I have ₹10'
>>> a = 10
>>> b = 20
>>> id(a)
4513131984
>>> id(b)
4513132304
>>> a = "svjkwnvklwvnlkwv"
>>> b = a
>>> id(a)
4532736552
>>> id(b)
4532736552
>>> 
