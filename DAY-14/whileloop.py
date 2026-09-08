'''
i = 1
while i <= 10:
    print(i)
    i += 1

i = 10
while i > 0:
    print(i)
    i -=1 

i = 5 
while i <= 50:
    print(i)
    i += 5

s = 'while loop'
i = 0 
while i < len(s):
    print(s[i])
    i+=1
i = len(s) - 1
while i >= 0:
    print(s[i])
    i -= 1

l = [5467, 5678, 6789, 987]
i = 0
while i < len(l):
    print(l[i])
    i += 1 

n =9876543256
s = 0
p = 1
while n > 0:
    print(n % 10)
    s = s + n % 10
    p = p * (n % 10)
    n//= 10
print("sum =", s)
print("Products =",p)


n = 876543456
res = 0
while n > 0:
    rem = n % 10
    #res = res * 10 + rem 
    if rem % 2 == 0:
        res = res * 10 + rem 
    n//= 10
print(res)
l = [7, 9, 23, 0 , 0, 0 , 13, 0 , 1, 0, 4, 0, 1, 0, 0, 1, 4, 5, 6,6, 13, 0]
i = 0
while 0 in l:
    l.remove(0) 
print(l) 
'''

l = [2,3,6,76,12,4,1,5,61,4,5,2,23]
i = 0
S = 0
while i <= len(l)-1:
    if l[i] != l[(len(l)-1) - i]:
        S = S + l[i] + l[(len(l)-1) - i]
        print(l[i])
        print(l[(len(l)-1) - i])
    S = S + l[i]  
    i +=1 
print(S)

