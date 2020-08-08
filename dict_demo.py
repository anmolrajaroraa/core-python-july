Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> employee = [101, "Ram", 15000, "Developer", "IT", 1234, 5677, 7808]
>>> student = [201, "Jenny", 12, "Non-medical", 95, 64, 70, 80, 90, 30, 73]
>>> employee = {

	}
>>> employee
{}
>>> type(employee)
<class 'dict'>
>>> employee = {
	"id" : 101,
	"name" : "Ram",
	"salary" : 15000,
	"designation" : "Developer",
	"department" : "IT"
	}
>>> employee
{'id': 101, 'name': 'Ram', 'salary': 15000, 'designation': 'Developer', 'department': 'IT'}
>>> employee[0]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    employee[0]
KeyError: 0
>>> employee['id']
101
>>> employee['name']
'Ram'
>>> del employee['department']
>>> employee
{'id': 101, 'name': 'Ram', 'salary': 15000, 'designation': 'Developer'}
>>> employee['department']
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    employee['department']
KeyError: 'department'
>>> employee['department'] = 'IT'
>>> employee
{'id': 101, 'name': 'Ram', 'salary': 15000, 'designation': 'Developer', 'department': 'IT'}
>>> employee['department'] = 'Finance'
>>> employee
{'id': 101, 'name': 'Ram', 'salary': 15000, 'designation': 'Developer', 'department': 'Finance'}
>>> 
>>> employee = {
	"id" : 101,
	"name" : "Ram",
	"salary" : 15000,
	"designation" : "Developer",
	"department" : "IT",
	"contact_1" : 1234,
	"contact_2" : 5677,
	"contact_3" : 7808
	}
>>> employee = {
	"id" : 101,
	"name" : "Ram",
	"salary" : 15000,
	"designation" : "Developer",
	"department" : "IT",
	"contact_1" : 1234
	}
>>> employee = {
	"id" : 101,
	"name" : "Ram",
	"salary" : 15000,
	"designation" : "Developer",
	"department" : "IT",
	"contact_1" : 1234,
	"contact_2" : 5677,
	"contact_3" : 7808
	}
>>> employee2 = {
	"id" : 102,
	"name" : "Anmol",
	"salary" : 25000,
	"designation" : "Developer",
	"department" : "IT",
	"contact_1" : 1234
	}
>>> employee["contact_1"]
1234
>>> employee["contact_2"]
5677
>>> employee2["contact_1"]
1234
>>> employee2["contact_2"]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    employee2["contact_2"]
KeyError: 'contact_2'
>>> employee = {
	"id" : 101,
	"name" : "Ram",
	"salary" : 15000,
	"designation" : "Developer",
	"department" : "IT",
	"contact" : [1234, 5677, 7808]
	}
>>> employee2 = {
	"id" : 102,
	"name" : "Anmol",
	"salary" : 25000,
	"designation" : "Developer",
	"department" : "IT",
	"contact" : [1234]
	}
>>> employee['contact']
[1234, 5677, 7808]
>>> employee2['contact']
[1234]
>>> employee['contact'][0]
1234
>>> student = {
	"id" : 201,
	"name" : "Jenny",
	"class" : 12,
	"stream" : "Non-medical",
	"marks" : {
		"english" : 95,
		"maths" : 64,
		"physics" : 70,
		"chemistry" : 80,
		"cs" : 90,
		"phd" : 30
		},
	"attendance" : 75
	}
>>> student["marks"]
{'english': 95, 'maths': 64, 'physics': 70, 'chemistry': 80, 'cs': 90, 'phd': 30}
>>> student["marks"]["cs"]
90
>>> len(student)
6
>>> for i in range(len(student)):
	print(i)

	
0
1
2
3
4
5
>>> for key in student:
	print(key)

	
id
name
class
stream
marks
attendance
>>> for key in student.keys():
	print(key)

	
id
name
class
stream
marks
attendance
>>> for key in student.values():
	print(key)

	
201
Jenny
12
Non-medical
{'english': 95, 'maths': 64, 'physics': 70, 'chemistry': 80, 'cs': 90, 'phd': 30}
75
>>> for key in student.items():
	print(key)

	
('id', 201)
('name', 'Jenny')
('class', 12)
('stream', 'Non-medical')
('marks', {'english': 95, 'maths': 64, 'physics': 70, 'chemistry': 80, 'cs': 90, 'phd': 30})
('attendance', 75)
>>> for pairin student.items():
	print(pair)
	
SyntaxError: invalid syntax
>>> 
>>> for pair in student.items():
	print(pair)

	
('id', 201)
('name', 'Jenny')
('class', 12)
('stream', 'Non-medical')
('marks', {'english': 95, 'maths': 64, 'physics': 70, 'chemistry': 80, 'cs': 90, 'phd': 30})
('attendance', 75)
>>> for value in student.values():
	print(value)

	
201
Jenny
12
Non-medical
{'english': 95, 'maths': 64, 'physics': 70, 'chemistry': 80, 'cs': 90, 'phd': 30}
75
>>> dir(dict)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> dict.fromkeys( [ "id", "name", "class", "stream", "marks", "attendance" ] )
{'id': None, 'name': None, 'class': None, 'stream': None, 'marks': None, 'attendance': None}
>>> 
>>> student.keys()
dict_keys(['id', 'name', 'class', 'stream', 'marks', 'attendance'])
>>> keys = student.keys()
>>> 
>>> dict.fromkeys( keys )
{'id': None, 'name': None, 'class': None, 'stream': None, 'marks': None, 'attendance': None}
>>> 
>>> dict.fromkeys("id")
{'i': None, 'd': None}
>>> dict.fromkeys( ["id"] )
{'id': None}
>>> 
>>> dict.fromkeys( keys, 'NA' )
{'id': 'NA', 'name': 'NA', 'class': 'NA', 'stream': 'NA', 'marks': 'NA', 'attendance': 'NA'}
>>> student = dict.fromkeys( keys, 'NA' )
>>> student
{'id': 'NA', 'name': 'NA', 'class': 'NA', 'stream': 'NA', 'marks': 'NA', 'attendance': 'NA'}
>>> student['id'] = 101
>>> student
{'id': 101, 'name': 'NA', 'class': 'NA', 'stream': 'NA', 'marks': 'NA', 'attendance': 'NA'}
>>> student['id']
101
>>> student.get('id')
101
>>> student.pop('id')
101
>>> student
{'name': 'NA', 'class': 'NA', 'stream': 'NA', 'marks': 'NA', 'attendance': 'NA'}
>>> student["attendance"] = 75
>>> student["attendance"] = "Insufficient data"
>>> student
{'name': 'NA', 'class': 'NA', 'stream': 'NA', 'marks': 'NA', 'attendance': 'Insufficient data'}
>>> student["attendance"] = "NA"
>>> student["attendance"] = 75
>>> student.setdefault('attendance', 'Insufficient data')
75
>>> student
{'name': 'NA', 'class': 'NA', 'stream': 'NA', 'marks': 'NA', 'attendance': 75}
>>> student.setdefault('id', 'NA')
'NA'
>>> student
{'name': 'NA', 'class': 'NA', 'stream': 'NA', 'marks': 'NA', 'attendance': 75, 'id': 'NA'}
>>> student['id'] = 101
>>> student
{'name': 'NA', 'class': 'NA', 'stream': 'NA', 'marks': 'NA', 'attendance': 75, 'id': 101}
>>> employee
{'id': 101, 'name': 'Ram', 'salary': 15000, 'designation': 'Developer', 'department': 'IT', 'contact': [1234, 5677, 7808]}
>>> employee.update(employee2)
>>> employee
{'id': 102, 'name': 'Anmol', 'salary': 25000, 'designation': 'Developer', 'department': 'IT', 'contact': [1234]}
>>> 
>>> 
>>> employee3 = {
	"id" : 103,
	"cabin_no" : 9
}
>>> employee.update(employee3)
>>> employee
{'id': 103, 'name': 'Anmol', 'salary': 25000, 'designation': 'Developer', 'department': 'IT', 'contact': [1234], 'cabin_no': 9}
>>> 
