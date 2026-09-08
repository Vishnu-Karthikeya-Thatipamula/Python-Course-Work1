
import sys
print(sys.argv)
print(sys.version)
print(sys.path)
print("start")
print("end")


import math
print(math.sqrt(16))
print(math.factorial(5))
print(math.gcd(12, 18))
print(math.sin(math.pi/2))
print(math.cos(0))
print(math.tan(math.pi/4))
print(math.log(100, 10))
print(math.exp(2))
print(math.degrees(math.pi/2))
print(math.radians(180))
print(math.pow(2, 3))

import math

print(math.floor(12.00000000000000001))
print(math.floor(12.3))
print(math.floor(12.6666))
print(math.floor(12.99999999999999999))


print(math.ceil(12.00000000000000001))
print(math.ceil(12.3))
print(math.ceil(12.6666))
print(math.ceil(12.99999999999999999))

print(round(12.00000000000000001))
print(round(12.3))
print(round(12.6666))
print(round(12.99999999999999999))


import random

random.seed(9)
print(random.random())
print(random.randint(1, 10))
print(random.uniform(1, 10))
print(random.choice(['rock', 'Paper', 'Scissors']))
print(random.choices(['Python', 'java', 'CSS', 'HTML', 'JavaScript'], k=2))
print(random.shuffle(['Python', 'java', 'CSS', 'HTML', 'JavaScript']))

from collections import Counter, defaultdict
s = 'python programming'
res = Counter(s)
print(res)
d = {}
for char in s:
    d[char] = d.get(char, 0) + 1

print(d)    

product = ['sugar', 'milk', 'butter', 'eggs', 'flour']
res = defaultdict(list)
for i in product:
    res[i[0]].append(['des','rev','com'])
print(res)

s = 'python programming'
res = defaultdict(int)
for char in s:
    res[char] += 1  
print(res)

from collections import deque
d = deque() 
d.append(1)
d.append(2)
d.append(3)
d.append(4)
d.popleft()
d.pop()
d.append(5)
print(d)
