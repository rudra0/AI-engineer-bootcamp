balance = 1000
question = input("Enter the selection number: 1. Deposit 2. Withdraw 3. Check Balance: ")
if question == '1':
    amount = float(input("Enter the amount to deposit: "))
    balance += amount
    print("Deposit successful. Your new balance is:", balance)
elif question == '2':
    amount = float(input("Enter the amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds. Your current balance is:", balance)
    else:
        balance -= amount
        print("Withdrawal successful. Your new balance is:", balance)
elif question == '3': 
    print("Your current balance is:", balance)
else:    print("Invalid selection. Please enter 1, 2, or 3.")