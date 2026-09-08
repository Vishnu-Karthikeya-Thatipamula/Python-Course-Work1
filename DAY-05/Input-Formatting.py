Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#int float complex str list tuple set dictionary
a = input()
codegnan
a
'codegnan'
a = input()
1234
a
'1234'
a = input("Enter the marks:")
Enter the marks:60
a
'60'
Marks = int(input("Enter the marks:"))
Enter the marks:993
Marks
993
CGPA = float(input("Enter the CGPA:"))
Enter the CGPA:65.4
CGPA
65.4
College = str(input("Enter the name of the College:"))
Enter the name of the College: Kamala Instistute of technology & Science
College
' Kamala Instistute of technology & Science'
names = input()
Vishnu Karthikeya Shiva
names
'Vishnu Karthikeya Shiva'
names.split()
['Vishnu', 'Karthikeya', 'Shiva']
courses = 'python-java-c++-flask'
courses.split('-')
['python', 'java', 'c++', 'flask']
softskills = 'communication quickleaner'
softskills.split()
['communication', 'quickleaner']
names = input("Enter the names").split()
Enter the names
names = input("Enter the names:").split()
Enter the names: Vishnu Karthikeya Shiva
names
['Vishnu', 'Karthikeya', 'Shiva']
names = set(input("Enter the names
                  
SyntaxError: unterminated string literal (detected at line 1)
names = set(input("Enter the names:")).split
                  
Enter the names:Vishnu Karthikeya Shiva
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    names = set(input("Enter the names:")).split
AttributeError: 'set' object has no attribute 'split'
names = set(input("Enter the names:")).split
                  
Enter the names: {'Vishnu', 'Karthikeya', 'Shiva'}
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    names = set(input("Enter the names:")).split
AttributeError: 'set' object has no attribute 'split'
names = set(input("Enter names: ").split())
print(names)
                  
SyntaxError: multiple statements found while compiling a single statement
names = set(input("Enter names: ").split())
                  
Enter names: Kamala Instistute of technology
names
                  
{'of', 'Kamala', 'technology', 'Instistute'}
OTP = tuple(input("Enter the OTP:").split())
                  
Enter the OTP: 5 1 2 3
print("OTP:"OTP)
                  
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("OTP:",OTP)
                  
OTP: ('5', '1', '2', '3')
marks = input().split()
                  
12 11 15 16 18 
marks
                  
['12', '11', '15', '16', '18']
map(int,marks)
                  
<map object at 0x00000200596A3C40>
list(map(int,marks))
                  
[12, 11, 15, 16, 18]
marks = list(map(int,input("Enter the marks:"),marks.split()))
                  
Enter the marks: 12 11 15 16 18
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    marks = list(map(int,input("Enter the marks:"),marks.split()))
AttributeError: 'list' object has no attribute 'split'
marks = list(map(int,input("Enter the marks:").split()))
                  
Enter the marks:12 11 15 16 18
marks
                  
[12, 11, 15, 16, 18]
marks = tuple(map(int,input("Enter the marks:").split()))
                  
Enter the marks:12 11 15 16 18
marks
                  
(12, 11, 15, 16, 18)
marks = set(map(int,input("Enter the marks:").split()))
                  
Enter the marks: 12 11 15 16 18
marks
                  
{11, 12, 15, 16, 18}
Salary = float(map(int,input("Enter the Salary:").split()))
                  
Enter the Salary: 12000 16000 15000 48000 10000
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    Salary = float(map(int,input("Enter the Salary:").split()))
TypeError: float() argument must be a string or a real number, not 'map'
Salary = float(int,input("Enter the Salary:").split())
                  
Enter the Salary: 12000 16000 15000 48000 10000
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    Salary = float(int,input("Enter the Salary:").split())
TypeError: float expected at most 1 argument, got 2
Salary = set(map(float,input("Enter the marks:").split()))
                  
Enter the marks: 12.5 18.3 15.9 15.5 17.0
Salary
                  
{12.5, 15.5, 15.9, 17.0, 18.3}
a,b = [1,2]
                  
a
                  
1
b
                  
2
a,b,c =(1,12.3,"str")
                  
a
                  
1
b
                  
12.3
c
                  
'str'
email,password = input("Enter the Email and password:").split()
                  
Enter the Email and password: vishnu@gmail.com Vishnu@134
email
                  
'vishnu@gmail.com'
password
                  
'Vishnu@134'
name, marks = input("Enter the name and marks:").split()
                  
Enter the name and marks: Micheal  100
name
                  
'Micheal'
marks
                  
'100'
int(marks)
                  
100
a,b,c = list(map(int,input().split()))
                  
12 13 14
a
                  
12
b
                  
13
c
                  
14
status = eval(input())
                  
status = eval(input())
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    status = eval(input())
  File "<string>", line 1
    status = eval(input())
                  ^^^^^
SyntaxError: invalid syntax. Did you mean 'not'?
>>> status = eval(input())
...                   
True
>>> status
...                   
True
>>> type(status)
...                   
<class 'bool'>
>>> status = eval(input())
...                   
[1,2,3,4]
>>> ststus = eval(input())
...                   
status = eval(input())
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    ststus = eval(input())
  File "<string>", line 1
    status = eval(input())
                  ^^^^^
SyntaxError: invalid syntax. Did you mean 'not'?
>>> status = eval(input())
...                   
2+3j
>>> type(status)
...                   
<class 'complex'>
>>> status = eval(input())
...                   
{'ZIP', 'ZAP', 'VIP'}
>>> type(status)
...                   
<class 'set'>
>>> status = eval(input())
...                   
('12', 'jan', '15', 'Feb', '13', 'Nov')
>>> type(status)
...                   
<class 'tuple'>
>>> status = eval(input())
...                   
college
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    status = eval(input())
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'college' is not defined. Did you mean: 'College'?
>>> status = eval(input())
...                   
College
>>>      
... type(status)
...                   
<class 'str'>
