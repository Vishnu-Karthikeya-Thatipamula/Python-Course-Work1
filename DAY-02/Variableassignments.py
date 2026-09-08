Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
>>> print("hello");
hello
>>> '''
... Multiy line
... comment
... '''
'\nMultiy line\ncomment\n'
>>> 
>>> ['False', 'None','True','and', 'or', 'not','break', 'continue', 'def', 'as', 'assert', 'async', 'await',
... 
... 
... import
... 
... print(keyword.kwlist)
... print(len(keyword.kwlist))
SyntaxError: '[' was never closed
>>> import
... 
... print(keyword.kwlist)
... print(len(keyword.kwlist))SyntaxError: '[' was never closed
SyntaxError: Expected one or more names after 'import'
>>> 
>>> 
>>> 
=============================================================================================== RESTART: Shell ===============================================================================================
>>> a = 10
>>> a=b=c=10
>>> a
10
>>> b
10
>>> c
10
>>> a,b,c = 10,20,30
>>> a
10
>>> b
20
>>> c
30
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> K = 5
>>> V = 6
>>> K,V = V,K
>>> k
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    k
NameError: name 'k' is not defined. Did you mean: 'K'?
>>> K
6
>>> V
5
