Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1 = [10,20,30,]
>>> list1 = [10,20,30,'forty',True,[123,234,345]]
>>> list1.append(1000)
>>> list1.append([121,232,343])
>>> list1.extened([121,232,343])
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    list1.extened([121,232,343])
AttributeError: 'list' object has no attribute 'extened'
>>> list1.extend([121,232,343])
>>> list1
[10, 20, 30, 'forty', True, [123, 234, 345], 1000, [121, 232, 343], 121, 232, 343]
>>> del list1[2]
>>> list1
[10, 20, 'forty', True, [123, 234, 345], 1000, [121, 232, 343], 121, 232, 343]
>>> list1.clear()
>>> list1
[]
>>> del list1
>>> list1
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    list1
NameError: name 'list1' is not defined
>>> list1 = [10,20,30,'forty',True,[123,234,345], 1000, [121, 232, 343], 121, 232, 343]
>>> list2 = list1
>>> list3 = list1.copy()
>>> import copy
>>> list4 = copy.deepcopy(list1)
>>> list1
[10, 20, 30, 'forty', True, [123, 234, 345], 1000, [121, 232, 343], 121, 232, 343]
>>> list2
[10, 20, 30, 'forty', True, [123, 234, 345], 1000, [121, 232, 343], 121, 232, 343]
>>> list3
[10, 20, 30, 'forty', True, [123, 234, 345], 1000, [121, 232, 343], 121, 232, 343]
>>> list4
[10, 20, 30, 'forty', True, [123, 234, 345], 1000, [121, 232, 343], 121, 232, 343]
>>> del list1[2]
>>> list1
[10, 20, 'forty', True, [123, 234, 345], 1000, [121, 232, 343], 121, 232, 343]
>>> list2
[10, 20, 'forty', True, [123, 234, 345], 1000, [121, 232, 343], 121, 232, 343]
>>> list3
[10, 20, 30, 'forty', True, [123, 234, 345], 1000, [121, 232, 343], 121, 232, 343]
>>> list4
[10, 20, 30, 'forty', True, [123, 234, 345], 1000, [121, 232, 343], 121, 232, 343]
>>> list1[4].append(999)
>>> list1
[10, 20, 'forty', True, [123, 234, 345, 999], 1000, [121, 232, 343], 121, 232, 343]
>>> list2
[10, 20, 'forty', True, [123, 234, 345, 999], 1000, [121, 232, 343], 121, 232, 343]
>>> list3
[10, 20, 30, 'forty', True, [123, 234, 345, 999], 1000, [121, 232, 343], 121, 232, 343]
>>> list4
[10, 20, 30, 'forty', True, [123, 234, 345], 1000, [121, 232, 343], 121, 232, 343]
>>> list4.count(121)
1
>>> list4.count(1)
1
>>> int(True)
1
>>> int(False))
SyntaxError: invalid syntax
>>> int(False)
0
>>> list4.count(True)
1
>>> list4.index(1)
4
>>> list4.index(0)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    list4.index(0)
ValueError: 0 is not in list
>>> list4.index(1)
4
>>> list4.index(1, 5)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    list4.index(1, 5)
ValueError: 1 is not in list
>>> list4
[10, 20, 30, 'forty', True, [123, 234, 345], 1000, [121, 232, 343], 121, 232, 343]
>>> list4.insert(3, 40)    # index, object
>>> list4
[10, 20, 30, 40, 'forty', True, [123, 234, 345], 1000, [121, 232, 343], 121, 232, 343]
>>> list4[5] = False    # overwriting
>>> list4
[10, 20, 30, 40, 'forty', False, [123, 234, 345], 1000, [121, 232, 343], 121, 232, 343]
>>> del list4[3]
>>> list4.pop()   # pop from end
343
>>> list4.pop()   # pop from end
232
>>> list4.pop()   # pop from end
121
>>> list4
[10, 20, 30, 'forty', False, [123, 234, 345], 1000, [121, 232, 343]]
>>> list4.pop(2)
30
>>> # list4.remove()    # removes a particular value
>>> list4.append(1000)
>>> list4
[10, 20, 'forty', False, [123, 234, 345], 1000, [121, 232, 343], 1000]
>>> list4.remove(1000)
>>> list4
[10, 20, 'forty', False, [123, 234, 345], [121, 232, 343], 1000]
>>> list4[::-1]
[1000, [121, 232, 343], [123, 234, 345], False, 'forty', 20, 10]
>>> list4
[10, 20, 'forty', False, [123, 234, 345], [121, 232, 343], 1000]
>>> list4.reverse()
>>> list4
[1000, [121, 232, 343], [123, 234, 345], False, 'forty', 20, 10]
>>> list4.sort()
Traceback (most recent call last):

  File "<pyshell#62>", line 1, in <module>
    list4.sort()
TypeError: '<' not supported between instances of 'list' and 'int'
>>> 
>>> list5 = [464,365,355465,5643,6576,34,4676,6,66543]
>>> list5.sort()
>>> list5
[6, 34, 365, 464, 4676, 5643, 6576, 66543, 355465]
>>> list5 = [464,365,355465,5643,6576,34,4676,6,66543]
>>> list5.sort( reverse=True )   #descending order
>>> list5
[355465, 66543, 6576, 5643, 4676, 464, 365, 34, 6]
>>> tuple1 = ( 123,234,345,'forty', (34,43,34,43), [45,56,67,78,89] )
>>> del tuple1[0]
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    del tuple1[0]
TypeError: 'tuple' object doesn't support item deletion
>>> dir(tuple)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> tuple1[4][0] = 999
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    tuple1[4][0] = 999
TypeError: 'tuple' object does not support item assignment
>>> tuple1[-1][0] = 999
>>> tuple1
(123, 234, 345, 'forty', (34, 43, 34, 43), [999, 56, 67, 78, 89])
>>> list5
[355465, 66543, 6576, 5643, 4676, 464, 365, 34, 6]
>>> tuple[-1] = list5
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    tuple[-1] = list5
TypeError: 'type' object does not support item assignment
>>> 
