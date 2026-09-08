
print("=======MENU========")
data = {
         'Facewash':80,
         'cookingoil':180,
         'Rice':500,
         'egg':36,
         'Milk':32,
         'coconutoil':50,
         'snacks':50,
         'sugar': 100
         
}
for i in data:
    print(i.ljust(20), data[i])

prods = input("Enter the products:").split()
prods_lst = list(prods)
total = 0
for i in prods_lst:
    print(i.ljust(20),data[i])
    total += data[i]
print("Your bill is ", total)




bill = 0
while True:
    prod = input("Enter the products name or [E]xit:")
    if prod == 'E' or prod == 'e':
        print("Thanks for shopping")
        print("Total bill", bill)
        break
    else:
        Q = int(input("Enter the Quantity:"))
        bill += data[prod] * Q
