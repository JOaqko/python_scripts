account = {
    "name": "Alice",
    "balance": 1000
}

def deposit(account, amount):
    account["balance"] += amount

def withdraw(account, amount):
    account["balance"] -= amount
    if account["balance"] < 0:
        print("Warning: Your account is overdrawn!")

def fee(account):
    account["balance"] -= 5  # Deduct $5 fee

def interest(account):
    account["balance"] += account["balance"] * 0.05  # Add 5% interest

operations = {
    "deposit": deposit,
    "withdraw": withdraw,
    "fee": fee,
    "interest": interest
}
while True:
    operation = input("Enter operation (deposit, withdraw, fee, interest) or 'exit' to quit: ")
    if operation == "exit":
        break
    if operation in ["deposit", "withdraw"]:
        amount = float(input("enter amount: "))
        operations[operation](account, amount)
        print(f"Current balance: {account['balance']}")
    elif operation in ["fee", "interest"]:
        operations[operation](account)
        print(f"Current balance: {account['balance']}")
    else:
        print("Invalid operation. Please try again.")
        