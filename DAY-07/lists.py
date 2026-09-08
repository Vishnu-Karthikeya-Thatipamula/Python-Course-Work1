Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l =[]
l = list()
type(l)
<class 'list'>
l = [1,12.3,"str",True,[1,2,3],(1,2,3),{1,2,3},{1:1,2:2,3:3,},3+8j]
l
[1, 12.3, 'str', True, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2, 3: 3}, (3+8j)]
l = [1,1,1,1]
l
[1, 1, 1, 1]
l = [1,12.3,"str",True,[1,2,3],(1,2,3),{1,2,3},{1:1,2:2,3:3},3+8j]
l=[1,1,1,1]
l
[1, 1, 1, 1]
a=[1,2,3]
b = [4,5,6]
a+b
[1, 2, 3, 4, 5, 6]
a*8
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
a[0]
1
a[15]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a[15]
IndexError: list index out of range
a[2]
3
a=[567,76,13,433,134,234]
a
[567, 76, 13, 433, 134, 234]
a[:3]
[567, 76, 13]
a[:1]
[567]
a[:2]
[567, 76]
a[:-2]
[567, 76, 13, 433]

a[-2:]
[134, 234]
a[-1:]
[234]
a[1,4]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a[1,4]
TypeError: list indices must be integers or slices, not tuple
a[1:4]
[76, 13, 433]
a[-2:3]
[]
a[1::2]
[76, 433, 234]
a[0:5:1]
[567, 76, 13, 433, 134]
a[::-1]
[234, 134, 433, 13, 76, 567]
#methods
max(a)
567
min(a)
13
sort(a)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    sort(a)
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
sorted(a)
[13, 76, 134, 234, 433, 567]
len(a)
6
a
[567, 76, 13, 433, 134, 234]
id(a)
2928274917376
a[0]
567
a[0] = 56
a
[56, 76, 13, 433, 134, 234]
id(a)
2928274917376
a.append(50)
a
[56, 76, 13, 433, 134, 234, 50]
a.insert(2,56)
a
[56, 76, 56, 13, 433, 134, 234, 50]
a.insert(1,14)
a
[56, 14, 76, 56, 13, 433, 134, 234, 50]
a.extent(55,66,11,22,33)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a.extent(55,66,11,22,33)
AttributeError: 'list' object has no attribute 'extent'. Did you mean: 'extend'?
a.extent([55,66,11,22,33])
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a.extent([55,66,11,22,33])
AttributeError: 'list' object has no attribute 'extent'. Did you mean: 'extend'?
a.extend([55,66,11,22,33])
a
[56, 14, 76, 56, 13, 433, 134, 234, 50, 55, 66, 11, 22, 33]
a.pop()
33
a.pop(5)
433
a.pop(0)
56
a
[14, 76, 56, 13, 134, 234, 50, 55, 66, 11, 22]
a.remove(66)
a
[14, 76, 56, 13, 134, 234, 50, 55, 11, 22]
a.remove(11)
a
[14, 76, 56, 13, 134, 234, 50, 55, 22]
>>> del a[1]
>>> a
[14, 56, 13, 134, 234, 50, 55, 22]
>>> a.clear()
>>> a
[]
>>> id(a)
2928274917376
>>> del [0:3]
SyntaxError: invalid syntax
>>> del a[0:3]
>>> a
[]
>>> del a[:3]
>>> del b[:3]
>>> b
[]
>>> A = [55,55,44,77,58,64,48,638,]
>>> A
[55, 55, 44, 77, 58, 64, 48, 638]
>>> A.pop(8)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    A.pop(8)
IndexError: pop index out of range
>>> a.index(55)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a.index(55)
ValueError: list.index(x): x not in list
>>> 
>>> A.pop(55)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    A.pop(55)
IndexError: pop index out of range
>>> A.index(55)
0
>>> A.count(55)
2
>>> B =A
>>> B
[55, 55, 44, 77, 58, 64, 48, 638]
>>> C = A.copy()
>>> C.append(12)
>>> C
[55, 55, 44, 77, 58, 64, 48, 638, 12]
>>> A
[55, 55, 44, 77, 58, 64, 48, 638]
>>> any([1,'',False,[],(),{},set()])
True
>>> any([0,'',False,[],(),{},set()])
False
>>> all([1,'',True,[1],(5),{4:5},set(A)])
False
>>> sum(A)
1039
>>> A.sort()
>>> A
[44, 48, 55, 55, 58, 64, 77, 638]
>>> A.reverse()
>>> A
[638, 77, 64, 58, 55, 55, 48, 44]
