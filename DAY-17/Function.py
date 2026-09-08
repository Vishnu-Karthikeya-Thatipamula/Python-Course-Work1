'''
def functionname(arg):
    #stsmt
    return (opt)
    
functionname(parameter)


def gst(price):
    print("Original Price:", price)
    print("Final Price:",price + price *0.18)

gst(1000)
gst(5000)
gst(800)
gst(1500)
gst(20000)

def table(n):
    for i in range(1,11):
        print(n ,"*", i, "=", n*i)

table(25)
table(19)
table(75)

def is_leap(year):
    leap = False
    if (year % 4 == 0 and year % 100 == 0) and year % 400 == 0:
        leap = True
    else:
        leap = False   
    # Write your logic here
    return leap

year = int(input())
print(is_leap(year))

def is_prime(n):
    prime = False
    count = 0
    for i in range(2,n):
        if n % i == 0:
            count+= 1
            
    if count > 0:
        prime = True  
    else:
        prime = False

    return prime

n = int(input("Enter the number:"))
print(is_prime(n))



def display(name,email,pwd):
    print("name:",name)
    print("email:",email)
    print("pwd:",pwd)

display('dinesh','dinesh@gmail.com','dinesh@123')
display('dinesh@gmail.com', 'dinesh','dinesh@123')
display('dinesh@123','dinesh','dinesh@gmail.com')

display(name='dinesh',email='dinesh@gmail.com',pwd='dinesh@123')
display(email='dinesh@gmail.com', name='dinesh',pwd='dinesh@123')
display(pwd='dinesh@123',name='dinesh',email='dinesh@gmail.com')

display("dinesh", "email")
display("dinesh")

def display(*names):
    print(names)
display("dinesh")
display("dinesh", "teja")
display("dinesh", "teja","dipak")
display("dinesh", "teja","dipak","vishnu")
'''
def display(**names):
    print(names)

display(n1 = "dinesh")
display(n1="dinesh", n2="teja")