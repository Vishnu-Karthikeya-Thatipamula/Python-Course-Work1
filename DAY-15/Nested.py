
for i in range(5):
    for j in range(3):
        print(j, end =' ')
    print()

for i in range(5):
    for j in range(5):
        print("*", end=' ')
    print()


for i in range(5):
    for j in range(1,5):
        print("*", end=' ')
    print()


for i in range(5):
    for j in range(5):
        if j % 2 == 0:
            print("0", end=" ")
        else:
            print("1", end = " ")
    print()

for i in range(5):
    for j in range(5):
        if i % 2 == 0:
            print("0", end=" ")
        else:
            print("1", end = " ")
    print()


   
for i in range(5):
    for j in range(5):
        if (i % 2 == 0 and j % 2 == 0) or (i % 2!= 0 and j % 2 != 0):
            print("0", end=" ")
        else:
            print("1", end = " ")

    print()
        


for i in range(5):
    for j in range(5):
        print(i+j, end = " ")
    print()


count = 1
for i in range(5):
    for j in range(5):
        print(count, end=" ")
        count +=1
    print()

count = 1
for i in range(5):
    for j in range(count):
        print("*", end =" ")
    print()
    count += 1 

count = 5
for i in range(5):
    for j in range(count):
        print("*", end =" ")
    print()
    count -= 1 

count = 1
for i in range(5):
    for j in range(count):
        print("*", end =" ")
    print()
    count += 1


for i in range(5):
    for p in range(5 - i - 1):
        print(' ',end = " ")
    for j in range(i + 1):
        print("*", end = " ")
    print()

n = int(input("Enter the range:"))
for i in range(n):
    for p in range(i):
        print(' ', end = " ")
    for j in range( n - i):
        print("*", end= " ")
    print()

count = 1
n = int(input("Enter the range:"))
m = n // 2 
for i in range(n):
    if i <= m:
        print("* "*(i+1), end = " ")
    else:
        print("* "*(n - i), end =" ")
    print()

count = 1
n = int(input("Enter the range:"))
m = n // 2 
for i in range(n):
    if i in range(n):
        if i <= m:
            print(' '*(m-i), "* "*(i+1),end = " ",sep=" ")
        else:
            print(" "*(i-m ),"* "*(n - i), end=" ", sep=' ')
    print()
