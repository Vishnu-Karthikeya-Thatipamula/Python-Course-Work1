from datetime import date ,time,datetime, timedelta
t = date.today()
print(t)
print(t.day)
print(t.month)
print(t.year)
print(t.weekday())
year,month,day = list(map(int,input("Enter the date of birth in format of [yyyy-MM-DD]:").split('-')))
if 1 <= month <= 12 and 1980 <= year <= 2020 and 1<= day <= 31:
    print("Valid DOB")
else:
    print("Invalid DOB")

tm= time(23,6,6)
print(tm)
print(tm.hour)
print(tm.minute)
print(tm.second)

dt = datetime.now()
print(dt)
print(dt.strftime('%d-%m-%Y'))
print(dt.strftime('%d-%m-%Y %H:%M-%S'))
print(dt.strftime('%d-%m-%Y %H:%M-%S %p'))
print(dt.strftime('%d-%m-%Y %I:%M-%S %p'))
print(dt.strftime('%d-%b-%Y %I:%M-%S %p'))
print(dt.strftime('%d-%B-%Y %I:%M-%S %p'))
print(dt.strftime('%a,%d-%B-%Y %I:%M-%S %p'))
print(dt.strftime('%A, %d-%B-%Y %I:%M-%S %p'))

dt = datetime.now()
t = date.today()
t7 = t + timedelta(days = 7)
m15 = dt + timedelta(minutes = 15)
print(t7, m15)

from itertools import permutations, combinations 

s = 'abc'
res1 = list(permutations(s,2))
res2 = list(combinations(s,2))
print([''.join(i) for i in res1])
print([''.join(i) for i in res2])


