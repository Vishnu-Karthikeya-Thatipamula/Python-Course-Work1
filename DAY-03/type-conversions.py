a = 10
float(a) #conversion into float
10.0
str(a)  #conversion into str
'10'
complex(a) #conversion into complex

(10+0j)
bool(a) #conversion into Boolean
True
list(a) #conversion into list
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    list(a) #conversion into list
TypeError: 'int' object is not iterable
set(a) #conversion into set
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    set(a) #conversion into set
TypeError: 'set' object is not callable
dict(a) #conversion into dictionary
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    dict(a) #conversion into dictionary
TypeError: 'int' object is not iterable
>>> b= 10.3
>>> float(b) #conversion into int
10.3
>>> int(b) #conversion into int
10
>>> complex(b) #conversion into complex
(10.3+0j)
>>> bool(b) #conversion into Boolean
True
>>> list(b) #conversion into list
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    list(b) #conversion into list
TypeError: 'float' object is not iterable
>>> set(b) #conversion into set
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    set(b) #conversion into set
TypeError: 'set' object is not callable
>>> dict(b) #conversion into dictionary
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    dict(b) #conversion into dictionary
TypeError: 'float' object is not iterable
>>> int(c) #conversion into int
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    int(c) #conversion into int
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> c = 30 + 5j
>>> int(c) #conversion into int
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    int(c) #conversion into int
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> float(c) #conversion into float
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    float(c) #conversion into float
TypeError: float() argument must be a string or a real number, not 'complex'
>>> boolean(c) #conversion into Boolean
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    boolean(c) #conversion into Boolean
NameError: name 'boolean' is not defined
>>> KeyboardInterrupt
>>> KeyboardInterrupt
>>> str(c) #conversion into string
'(30+5j)'
>>> list(c) # conversion into list
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    list(c) # conversion into list
TypeError: 'complex' object is not iterable
>>> dict(c) #conversion into dictionary
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    dict(c) #conversion into dictionary
TypeError: 'complex' object is not iterable
>>> set(a) #conversion into set
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    set(a) #conversion into set
TypeError: 'set' object is not callable
