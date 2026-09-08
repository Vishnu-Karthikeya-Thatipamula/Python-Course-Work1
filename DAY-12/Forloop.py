#Iteratable datatypes are string, tuple, list, set, dictionary, range
'''
str = "Vishnu karthikeya" #for string
for char in str:
    print(char)

names = ["Alice", "Bob", "Charlie", "David", "Eve"] #for list
for name in names:
    print(f"Hello, {name}!")

subject = ("Math", "Science", "History", "English") #for tuple
for sub in subject:
    print(f"Subject: {sub}")

set = {1,5,6,7,78,9,99,5,55,11} #for set
for num in set:
    print(f"Number: {num}") 

dict = {"name": "Alice", "age": 25, "city": "New York"} #for dictionary
for key, value in dict.items():
    print(f"{key}: {value}")
'''
'''
d = {1:1, 2:4, 3:9, 4:16, 5:25} #for dictionary
#for key, value in d.items(): Also we can use this method to print the key and value of dictionary
for k in d:
    #print(f"{key}: {value}") Same as above
    print(k,":",d[k])
'''

#Range() : Allows us to generate a sequence of numbers, which can be used in for loops or other iterable contexts.
#The range() function takes up to three arguments: start, stop, and step. The start argument specifies the starting value of the sequence (inclusive), the stop argument specifies the ending value of the sequence (exclusive), and the step argument specifies the increment between each value in the sequence.
#The range() function returns an iterable object that generates the sequence of numbers on-the-fly.
'''
for i in range(1, 11): #for range
    print(i)

for i in range(2,21,2): #for range with step
    print(i)

for i in range(5,101,5): #for range with step
    print(i)

for i in range(5, 0, -1): #for range with step
    print(i)

for i in range(19, 0, -2): #for range with step
    print(i)

str = "Vishnu karthikeya" #To print char with its index
for char in range(len(str)):
    print(char,str[char])

names = ["Alice", "Bob", "Charlie", "David", "Eve"] #To print list with its index
for name in range(len(names)):
    print(f"Hello, {names} ,{name}!")


subject = ("Math", "Science", "History", "English") #To print tuple with its index
for sub in range(len(subject)):
    print(f"Subject: {sub} , {subject}")


subject = ("Math", "Science", "History", "English") #To print tuple with its index
for sub in enumerate(subject):
    print(f"{sub}")


d = {1:1, 2:4, 3:9, 4:16, 5:25} #for dictionary
#for key, value in d.items(): Also we can use this method to print the key and value of dictionary
for k in enumerate(d):
    #print(f"{key}: {value}") Same as above
    print(k[0],k[1], d[k[1]])


for i in range(1,11): #break : It breaks the given loop when a given condition is true
    if i == 5:
        break
    print(i)

for i in range(1,11): #continue : It skips that particular loop at the particular condition`
    if i == 5:
        continue
    print(i)
'''
'''
for i in range(1,11): 
    if i == 5:
        break
    print(i)
else:
    print("End of the Loop")

for i in range(1, 11):
    if i == 5:
        print(i)
else:
    print("End of the Loop")

l = [12, 13, 14 , 15, 16, 17 , 18, 19]
n = 16 
for i in l:
    if i == n:
        print("16 is found (because, we stopped the loop with 'break' statement)")
        break

else:
    print(n, "not found (because we have not stopped the the loop with the 'break' statement)")
'''
'''
EPIN = 1234
for i in range(5):
    PIN = int(input("Enter the PIN:"))
    if PIN == EPIN:
        print("You are Welcome")
        break
    else:
        print("Invalid PIN")
else:
    print("Try again after 23 seconds")


#Check a number is prime or not
Num = int(input("Enter a number:"))
if Num % 2 != 0 and Num % 3 != 0 and Num % Num == 0 and Num % 1 == 0:
    print("Prime number")
else:
    print("Not a prime")

Num = int(input("Enter a number:"))
count = 0
for i in range(0, Num +1):
    if Num % i == 0:
        count += 1
if count > 2:
    print("It is prime number")
else:
    print("It is not a prime number")
'''

Num = int(input("Enter a number:"))
for i in range(2, Num // 2+1):
    if Num %i == 0:
        print("Not a prime")
        break
else:
    print("Prime Number")
