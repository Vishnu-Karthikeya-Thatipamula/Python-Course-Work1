'''
var = lambda arg: expression



wish = lambda name: f'Hello {name}, Good Morning'
name = input("Enter your name: ")
print(wish(name))

Gst = lambda price: price * 0.18
price = float(input("Enter the price: "))
print(f'Gst is: {Gst(price)}')

N = input("Enter a number: ")
iseven = lambda N: 'Even' if N % 2 == 0 else 'Odd'
print(iseven(int(N)))

a = input("Enter a character: ")
is_vowel = lambda a: 'Vowel' if a in 'aeiouAEIOU' else 'Consonant'
print(is_vowel(a))

x,y,z = 10,20,30
greatest = lambda x,y,z: x if (x>y and x>z) else (y if y>z else z)
print(greatest(x,y,z))



def update(l):
    for i in range(len(l)):
        l[i] = l[i] + 10
        return l
l = [1,2,3,4,5,6,7,8,9]

l = [1,2,3,4,5,6,7,8,9]

update = map(lambda x: x + 10, l)
print(list(update))

t = (789,421,3453, 24235,35430)
Discount = map(lambda x: x - x*10, t)
print(tuple(Discount))

P = [1,2,3,4,5,6,7,8,9]
Filter = filter(lambda x: x%2==0, P)
print(list(Filter))

D = (789,421,3453, 24235,35430)
GT = filter(lambda x: x>1000, D)
print(tuple(GT))

L = ['sowmya@codegnan.com','sowmya@yahoo.com','sowmya@gmail.com','sowmya@outlook.com']
Domain = map(lambda x: x.split('@')[1], L)
print(list(Domain))

'''

from functools import reduce
l = [4,2,4,64,75,2,4645,8]
res = reduce(lambda x,y: x+y, l)
print(res)
res1 = reduce(lambda prod, y: prod * y, l)
print(res1)


seat = {'s1':True, 's2':False, 's3':False, 's4':False, 's5':True, 's6':True}
Available_seats = filter(lambda i: seat[i] != True, seat)
print(list(Available_seats))

products = {'egg': 80,'sugar': 60,'salt': 20,'butter': 40,'milk': 30}
cost = filter(lambda i: products[i] > 50, products)
print(list(cost))
sorted_products = sorted(products.items(), key=lambda x: x[1])  #.items() returns a view object that displays a list of a dictionary's key-value tuple pairs. The sorted() function is used to sort the items based on the second element of each tuple (the value) using a lambda function as the key.
print(sorted_products)















































