Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Tuples (operators and methods)
#declaration
t= ()
t =tuple()
t = (1,2,3,45)
t
(1, 2, 3, 45)
t = (1)
#considered as integer. So,
t = (1,)
t = (1,1,1,1)
t
(1, 1, 1, 1)
t = (1, 23.4, 14 + 9j, "Vishnu", [1,2,3],(1,4,3), {1,7,102}, [1:5,77:98])
SyntaxError: invalid syntax
t = (1, 23.4, 14 + 9j, "Vishnu", [1,2,3],(1,4,3), {1,5,45})
t
(1, 23.4, (14+9j), 'Vishnu', [1, 2, 3], (1, 4, 3), {1, 45, 5})
type(t)
<class 'tuple'>
(1,2,3) + (4,5,6)
(1, 2, 3, 4, 5, 6)
(1,2,3) * 4
(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
t
(1, 23.4, (14+9j), 'Vishnu', [1, 2, 3], (1, 4, 3), {1, 45, 5})
t[1]
23.4
t[-1]
{1, 45, 5}
t[-3]
[1, 2, 3]
t[:-1:1]
(1, 23.4, (14+9j), 'Vishnu', [1, 2, 3], (1, 4, 3))
t[::2]
(1, (14+9j), [1, 2, 3], {1, 45, 5})
t[:2:]
(1, 23.4)
t[1:2:]
(23.4,)
t[3:4]
('Vishnu',)
t[3:]
('Vishnu', [1, 2, 3], (1, 4, 3), {1, 45, 5})
'Vishnu' in t
True
'Hiest' in t
False
15 not in t
True
45 in t
False
1 not in t
False
t = (12,789, 32, 13, 76,32, 453, 123, 7898, 1391,32)
t
(12, 789, 32, 13, 76, 32, 453, 123, 7898, 1391, 32)
sorted(t)
[12, 13, 32, 32, 32, 76, 123, 453, 789, 1391, 7898]
max(t)
7898
min(t)
12
len(t)
11
t
(12, 789, 32, 13, 76, 32, 453, 123, 7898, 1391, 32)
t.index(32)
2
sum(t)
10851
t.find(5)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    t.find(5)
AttributeError: 'tuple' object has no attribute 'find'
t[1]
789
t[1].append()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    t[1].append()
AttributeError: 'int' object has no attribute 'append'
>>> t[1].append(1)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    t[1].append(1)
AttributeError: 'int' object has no attribute 'append'
>>> t = ([1,2,3], 1,55,87,96,4)
>>> t[0].append(5)
>>> t
([1, 2, 3, 5], 1, 55, 87, 96, 4)
>>> #set
>>> s = {}
>>> type(s)
<class 'dict'>
>>> s ={1,2,3,4,5,6,134124,2345234,312,124}
>>> s
{1, 2, 3, 4, 5, 6, 134124, 2345234, 312, 124}
>>> s = {1,1,1,1,1}
>>> s
{1}
>>> s = set()
>>> s.add(1)
>>> s.add(12.3)
>>> s.add("str")
>>> s
{1, 12.3, 'str'}
>>> {1, 12.3, 'str'}
{1, 12.3, 'str'}
>>> #Uniques values are allowed, unodered, mutable elements are non allowed.
>>> s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    s.add([1,2,3])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
>>> s.add(False)
>>> s
{False, 1, 12.3, 'str'}
>>> s.add({1:1})
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    s.add({1:1})
TypeError: cannot use 'dict' as a set element (unhashable type: 'dict')
>>> s[0]
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    s[0]
TypeError: 'set' object is not subscriptable
>>> s[::1]
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    s[::1]
TypeError: 'set' object is not subscriptable
>>> s*4
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    s*4
TypeError: unsupported operand type(s) for *: 'set' and 'int'
>>> a = {1,2,3,4,5}
>>> b = {8,9,10,11,12,13}
>>> 2 in a
True
>>> 2 in b
False
>>> 3 not in b
True
>>> a|b
{1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 13}
a&b
set()
a - b
{1, 2, 3, 4, 5}
b - a
{8, 9, 10, 11, 12, 13}
a ^ b
{1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 13}
a
{1, 2, 3, 4, 5}
{1} => a
SyntaxError: cannot assign to set display
{1}<= a
True
{1,2,3} <= a
True
{12,13} <= a
False
a > {1,2,3}
True
a > {55, 7}
False
a >= {44, 1}
False
b.isdisjoint(a)
True
m = {'k', 'l', 'm', 'n'}
n = {'k','l'}
n.disjoint(m)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    n.disjoint(m)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
n.isdisjoint(m)
False
a = {12, 43,1, 7,89,40,23, 44}
a
{1, 7, 40, 43, 12, 44, 23, 89}
sorted(a)
[1, 7, 12, 23, 40, 43, 44, 89]
a(count(1))
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    a(count(1))
NameError: name 'count' is not defined. Did you mean: 'round'?
max(a)
89
min(a)
1
len(a)
8
a.index(a)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    a.index(a)
AttributeError: 'set' object has no attribute 'index'
all(a}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
all(a)
True
any(a)
True
b = a.copy()
b
{1, 7, 40, 43, 12, 44, 23, 89}
{1, 7, 40, 43, 12, 44, 23, 89}
{1, 7, 40, 43, 12, 44, 23, 89}
sum(a)
259
a.add(10)
a
{1, 7, 40, 10, 43, 12, 44, 23, 89}
b.add(100)
b
{1, 100, 7, 40, 43, 12, 44, 23, 89}
b.update({55,22,66,44,77})
b
{1, 66, 100, 7, 40, 43, 12, 44, 77, 55, 22, 23, 89}
b.pop()
1
b.pop()
66
b.pop()
100
b.remove(12)
b
{7, 40, 43, 44, 77, 55, 22, 23, 89}
b.remove(100)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    b.remove(100)
KeyError: 100
b.discard(100)
b
{7, 40, 43, 44, 77, 55, 22, 23, 89}
a.clear()
a
set()
