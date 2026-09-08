'''
def display():
    N = 10 #Local variable: accessible only in the function.
    print("Inside function:",n)
n =10 # Global varible : accessible throughou the program.
display(n)
print("Outside function:",n)

def display():
    global n 
    n = 10   # Adding keyword global will make the local variable accessible throughtout the program
    print("Inside function:",n)
 # Global varible : accessible throughou the program.
display()
print("Outside function:",n)

def display(n): #U cannot pass the global variable in the function as a parameter for a function
    global n 
    n+= 10   
    print("Inside function:", n) 
n = 10
display()
print("Outside function:",n)

def display():
    c = "PFS"
    def update(): # this is limited by scope resolution of the function 
        c = "JFS"
        print("Inner function:",c)
    update()
    print("Outer function:",c)
display()

#So, Inner function: JFS
    #Outer function: PFS


def display():
    c = "PFS"
    def update():
        nonlocal c    #keyword allows us to access the variable 
        c = "JFS"
        print("Inner function:",c)
    update()
    print("Outer function:",c)
display()

#So, Inner function: JFS
    #Outer function: JFS

l = [1,2,3,4,5]
print(max(l))

print = 20 # do not declare ur functions as the variables this will result in losing the scope of function and they malfunction.
print(max)

#Output:
#print(max)
#    ~~~~~^^^^^
#TypeError: 'int' object is not callable

'''
