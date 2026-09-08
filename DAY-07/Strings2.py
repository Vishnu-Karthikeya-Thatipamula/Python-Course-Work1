Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Whitespace and Trimming
s = ' Hello World '
s.strip()
'Hello World'
s.lstrip()
'Hello World '
s.rstrip()
' Hello World'
s.replace(' ','')
'HelloWorld'
#splitting and joining
s = 'Oracle-Google-Krafton-Santamonica-Microsoft'
s.split('-')
['Oracle', 'Google', 'Krafton', 'Santamonica', 'Microsoft']
s.rsplit('-')
['Oracle', 'Google', 'Krafton', 'Santamonica', 'Microsoft']
s.rsplit('-','2')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    s.rsplit('-','2')
TypeError: 'str' object cannot be interpreted as an integer
s.rsplit('-',2)
['Oracle-Google-Krafton', 'Santamonica', 'Microsoft']
''.join(s)
'Oracle-Google-Krafton-Santamonica-Microsoft'
'-'.join(s)
'O-r-a-c-l-e---G-o-o-g-l-e---K-r-a-f-t-o-n---S-a-n-t-a-m-o-n-i-c-a---M-i-c-r-o-s-o-f-t'
' '.join(s)
'O r a c l e - G o o g l e - K r a f t o n - S a n t a m o n i c a - M i c r o s o f t'
s.splitlines("-")
['Oracle-Google-Krafton-Santamonica-Microsoft']
s.splitlines(" ")
['Oracle-Google-Krafton-Santamonica-Microsoft']
s.splitlines()
['Oracle-Google-Krafton-Santamonica-Microsoft']
Y = "Vishnu Karthikeya"
Y.splitlines()
['Vishnu Karthikeya']
Y.splitlines(' ')
['Vishnu Karthikeya']
Y ="Vishnu\nKarthikeya"
Y.splitlines()
['Vishnu', 'Karthikeya']
'@'.join(s)
'O@r@a@c@l@e@-@G@o@o@g@l@e@-@K@r@a@f@t@o@n@-@S@a@n@t@a@m@o@n@i@c@a@-@M@i@c@r@o@s@o@f@t'
''.join(s)
'Oracle-Google-Krafton-Santamonica-Microsoft'
'A'.join(s)
'OArAaAcAlAeA-AGAoAoAgAlAeA-AKArAaAfAtAoAnA-ASAaAnAtAaAmAoAnAiAcAaA-AMAiAcArAoAsAoAfAt'
T = 'www.google.com.in'
T.partition('.')
('www', '.', 'google.com.in')
T.rpartition('.')
('www.google.com', '.', 'in')
T.startswith('www')
True
T.endswith('com')
False
'pynthv.13'.islower()
True
'Pythnv.13'.isupper()
False
'KING'.isupper()
True
'King'.islower()
False
'ABCDEFGH!@#$'.isalpha()
False
'abcdefghijk5788'.isalpha()
False
"ABCD".isalpha()
True
"isolate".isnum()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    "isolate".isnum()
AttributeError: 'str' object has no attribute 'isnum'. Did you mean: 'isalnum'?
>>> 'isolate'.isnum()
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    'isolate'.isnum()
AttributeError: 'str' object has no attribute 'isnum'. Did you mean: 'isalnum'?
>>> 'Isolate'.isalnum()
True
>>> 'isolate112'.isalnum()
True
>>> 'Isolate112@@@@'.isalnum()
False
>>> " ".isspace()
True
>>> "".ispace()
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    "".ispace()
AttributeError: 'str' object has no attribute 'ispace'. Did you mean: 'isspace'?
>>> "".isspace()
False
>>> "Peter Parker".isspace()
False
>>> "Peter ".isspace
<built-in method isspace of str object at 0x000001727BB65920>
>>> "Hello Boy".istitle()
True
>>> "is space".istitle()
False
>>> "Vishnu Karthikeya".istitle()
True
>>> "is that Khansar".istitle()
False
>>> "P))T Presentation".istitle()
True
>>> "s".identifier()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    "s".identifier()
AttributeError: 'str' object has no attribute 'identifier'. Did you mean: 'isidentifier'?
>>> 's'.isisidentifier()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    's'.isisidentifier()
AttributeError: 'str' object has no attribute 'isisidentifier'. Did you mean: 'isidentifier'?
>>> "s".isidentifier()
True
>>> "is".isidentifier()
True
>>> #isdecimal,isdigit, isnumeric
>>> '568974'isdigit()
SyntaxError: invalid syntax
>>> '568974'.isdigit()
True
>>> '987456'.isdecimal()
True
>>> 'ERTIUUUJSHGHJHYHHJ'.isdecimal()
False
>>> 'IV'.isnumeric()
False
>>> '789456123'.isnumeric()
True
