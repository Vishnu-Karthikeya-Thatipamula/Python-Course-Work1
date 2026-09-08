#if-else statement
usernmame = input("Enter your username: ")
password = input("Enter your password: ")
if usernmame == "admin" and password == "admin123":
    print("Welcome admin!") 
else:
    print("Invalid username or password. Access denied.")
    