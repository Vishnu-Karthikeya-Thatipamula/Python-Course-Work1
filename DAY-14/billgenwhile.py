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
