#int float complex string list tuple set dict frozenset
'''
def display(n):
    n += 20
    print("Inside:",n)
n = 10
print("Outside:",n)
display(n)

Outside: 10
Inside: 30

def display(n):
    n += 20.3
    print("Inside:",n)
n = 10.3
print("Outside:",n)
display(n)

Outside: 10.3
Inside: 30.6


def display(n):
    n += 20 + 5j
    print("Inside:",n)
n = 10 + 5j
print("Outside:",n)
display(n)

Outside: (10+5j)
Inside: (30+10j)


def display(n):
    n += "Morning"
    print("Inside:",n)
n = "Good"
display(n)
print("Outside:",n)


Outside: Good
Inside: GoodMorning


def display(n):
    n += [1,2,5]
    print("Inside:",n)
n = [10,3,45]
display(n)
print("Outside:",n)
Outside: [10, 3, 45, 1, 2,5]
Inside: [10, 3, 45, 1, 2, 5]


def display(n):
    n += (1,2,5)
    print("Inside:",n)
n = (10,3,45)
display(n)
print("Outside:",n)
Outside: (10, 3, 45)
Inside: (10, 3, 45, 1, 2, 5)

'''
def display(n):
    n= {1,2,5}
    n.union
    print("Inside:",n)
n = {10,3,45}
display(n)
print("Outside:",n)