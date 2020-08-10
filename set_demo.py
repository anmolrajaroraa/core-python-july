Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> set1 = {}
>>> type(set1)
<class 'dict'>
>>> set1 = set()
>>> set1
set()
>>> type(set1)
<class 'set'>
>>> set1 = {10, 20, 30}
>>> type(set1)
<class 'set'>
>>> set1
{10, 20, 30}
>>> set1 = {10, 20, 30, 'forty', 50.5, True, 'sixty', 'python', 'hello', 'Jenny', 'Ram', False, 1}
>>> set1
{'sixty', True, 'python', False, 'Ram', 10, 'hello', 'forty', 50.5, 20, 'Jenny', 30}
>>> set1 = {10, 20, 30, 'forty', 50.5, True, 'sixty', 'python', 'hello', 'Jenny', 'Ram', False, 1}
>>> set1
{'sixty', True, 'python', False, 'Ram', 10, 'hello', 'forty', 50.5, 20, 'Jenny', 30}
>>> set1 = {10, 20, 30, 'forty', 50.5, True, 'sixty', 'python', 'hello', 'Jenny', 'Ram', False, 1, 'Anna'}
>>> set1
{'sixty', True, 'python', False, 'Ram', 'Anna', 10, 'hello', 'forty', 50.5, 20, 'Jenny', 30}
>>> set1 = {10, 20, 30, 'forty', 50.5, True, 'sixty', 'python', 'hello', 'jenny', 'ram', False, 1, 'anna'}
>>> set1
{'sixty', True, 'python', False, 'anna', 10, 'hello', 'forty', 50.5, 20, 'jenny', 30, 'ram'}
>>> for value in set1:
	print(value)

	
sixty
True
python
False
anna
10
hello
forty
50.5
20
jenny
30
ram
>>> dir(set)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> set1.add("some text")
>>> set1
{'sixty', True, 'python', False, 'anna', 10, 'hello', 'forty', 50.5, 20, 'some text', 'jenny', 30, 'ram'}
>>> set2 = {'sixty', 'hello', 'jenny', 50.5, 'some text', 20, 'anna', 'Shyam'}
>>> set1 - set2
{False, True, 'python', 10, 'forty', 30, 'ram'}
>>> set2 - set1
{'Shyam'}
>>> set1.difference(set2)
{False, True, 'python', 10, 'forty', 30, 'ram'}
>>> set2.difference(set1)
{'Shyam'}
>>> set1
{'sixty', True, 'python', False, 'anna', 10, 'hello', 'forty', 50.5, 20, 'some text', 'jenny', 30, 'ram'}
>>> set2
{'sixty', 'anna', 'Shyam', 'hello', 50.5, 20, 'some text', 'jenny'}
>>> set3 = set2.difference(set1)
>>> set3
{'Shyam'}
>>> 
.difference_update(set1)
SyntaxError: invalid syntax
>>> set2.difference_update(set1)
>>> set2
{'Shyam'}
>>> set2.discard(10)
>>> set2
{'Shyam'}
>>> set1
{'sixty', True, 'python', False, 'anna', 10, 'hello', 'forty', 50.5, 20, 'some text', 'jenny', 30, 'ram'}
>>> set1.discard(10)
>>> set1
{'sixty', True, 'python', False, 'anna', 'hello', 'forty', 50.5, 20, 'some text', 'jenny', 30, 'ram'}
>>> set1.remove(10)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    set1.remove(10)
KeyError: 10
>>> set1.intersection(set2)
set()
>>> set2 = {'sixty', 'hello', 'jenny', 50.5, 'some text', 20, 'anna', 'Shyam'}
>>> set1.intersection(set2)
{'sixty', 'anna', 'hello', 50.5, 20, 'some text', 'jenny'}
>>> set1.union(set2)
{'sixty', True, 'python', False, 'forty', 20, 30, 'anna', 'Shyam', 'hello', 50.5, 'some text', 'jenny', 'ram'}
>>> set1.isdisjoint(set2)
False
>>> set3 = {111,222,333,444,555}
>>> set1.isdisjoint(set3)
True
>>> set1.issuperset(set2)
False
>>> set2 = {'sixty', 'hello', 'jenny', 50.5, 'some text', 20, 'anna'}
>>> set1.issuperset(set2)
True
>>> set2.issubset(set1)
True
>>> set1.pop()
'sixty'
>>> set1.pop()
True
>>> set1.pop()
'python'
>>> set1
{False, 'anna', 'hello', 'forty', 50.5, 20, 'some text', 'jenny', 30, 'ram'}
>>> (set1 - set2).union(set2 - set1)
{False, 'forty', 'sixty', 30, 'ram'}
>>> set1.symmetric
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    set1.symmetric
AttributeError: 'set' object has no attribute 'symmetric'
>>> set1.symmetric_difference(set2)
{'sixty', False, 'forty', 30, 'ram'}
>>> set2 = {'sixty', 'hello', 'jenny', 50.5, 'some text', 20, 'anna', 'Shyam'}
>>> (set1 - set2).union(set2 - set1)
{False, 'forty', 'sixty', 'Shyam', 30, 'ram'}
>>> set1.symmetric_difference(set2)
{'sixty', False, 'Shyam', 'forty', 30, 'ram'}
>>> frozenset(set1)
frozenset({False, 'anna', 'hello', 'forty', 50.5, 20, 'some text', 'jenny', 30, 'ram'})
>>> f_set = frozenset(set1)
>>> dir(f_set)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'copy', 'difference', 'intersection', 'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference', 'union']
>>> f_set.pop()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    f_set.pop()
AttributeError: 'frozenset' object has no attribute 'pop'
>>> 
