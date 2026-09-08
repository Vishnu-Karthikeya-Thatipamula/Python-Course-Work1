Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Output_formating
>>> a = 10
>>> b = 13.5
>>> c = 'codgnan'
>>> #comma separation print( a,b,c)
>>> print( a,b,c)
... 
10 13.5 codgnan
>>> print("a = ", a , "b =", b , "c =", c)
a =  10 b = 13.5 c = codgnan
>>> print("a = ", a , "b =", b , "c =", c, sep='')
a = 10b =13.5c =codgnan
>>> print("a = ", a , "b =", b , "c =", c, sep= '|')
a = |10|b =|13.5|c =|codgnan
>>> print("a = ", a , "b =", b , "c =", c, sep = '\n')
a = 
10
b =
13.5
c =
codgnan
>>> print("a = ", a , "b =", b , "c =", c sep = '\t')
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("a = ", a , "b =", b , "c =", c, sep = '\t')
a = 	10	b =	13.5	c =	codgnan
>>> print("a = ", a , "b =", b , "c =", c, sep = '\n\n')
a = 

10

b =

13.5

c =

codgnan
