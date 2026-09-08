Units = int(input("Enter the Units: "))
Senior_citizen = eval(input("Are you a senior citizen? (True/False): "))

#Allocation of the billing ranges
if Units <= 100 and Units > 0 :
    cost = 1.5
elif Units <= 200 and Units >= 101:
    cost = 2.5
elif Units <= 500 and Units >= 201:
    cost = 4.0
else:
    cost = 6.0

#Calculate bill_amount
bill_amount = Units * cost

#apply subsidy if Senior citizen
if Senior_citizen:
    bill_amount -=( bill_amount* 0.1)
#apply surcharge if units > 800
if Units > 800:
   bill_amount += (bill_amount * 0.5)

#Show the bill to user
print("Your bill is:", bill_amount)