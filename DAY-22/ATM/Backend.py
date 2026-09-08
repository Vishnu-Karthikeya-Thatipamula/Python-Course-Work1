data ={
    123456:{'name':'Dinesh', 'pin':1234, 'balance':1000, 'history':[]},
    234561:{'name':'Eshwar', 'pin':1234, 'balance':2000, 'history':[]},
    345612:{'name':'Sowmya', 'pin':1234, 'balance':3000, 'history':[]},     
}
def login():
    account_number = int(input("Enter your account number: "))
    pin = int(input("Enter your pin: "))
    if account_number in data and data[account_number]['pin'] == pin:
        print(f"Login sucessful!")
        return account_number
    else:
        print("Invalid account number or pin.")
        return None
    
def menu(account_number):
    while True:
        print(f"\nWelcome to ATM, {data[account_number]['name']}!")
        print("[C]heck Balance")
        print("[D]eposit")
        print("[W]ithdraw")
        print("[H]istory")
        print("[E]xit")
        choice = input("Enter your choice: ").upper()
        
        if choice == 'C':
            check_balance(account_number)
        elif choice == 'D':
            deposit(account_number)
        elif choice == 'W':
            withdraw(account_number)
        elif choice == 'H':
            transaction_history(account_number)
        elif choice == 'E':
            print("Thank you for using our ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def check_balance(account_number):
    balance = data[account_number]['balance']
    print(f"Your current balance is: {balance}")

def deposit(account_number):
    amount = float(input("Enter the amount to deposit: "))
    data[account_number]['balance'] += amount
    data[account_number]['history'].append(f"Deposited: {amount}")
    print(f"Successfully deposited {amount}. Your new balance is: {data[account_number]['balance']}")

def withdraw(account_number):
    amount = float(input("Enter the amount to withdraw: "))
    if amount <= data[account_number]['balance']:
        data[account_number]['balance'] -= amount
        data[account_number]['history'].append(f"Withdrew: {amount}")
        print(f"Successfully withdrew {amount}. Your new balance is: {data[account_number]['balance']}")
    else:
        print("Insufficient balance.")

def transaction_history(account_number):
    history = data[account_number]['history']
    if history:
        print("Transaction History:")
        for transaction in history:
            print(transaction)
    else:
        print("No transaction history available.")