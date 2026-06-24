balance = 1000.00
while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print("Deposit successful. Your new balance is:", balance)
    elif choice == '2':
        amount = float(input("Enter the amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds. Your current balance is:", balance)
        else:
            balance -= amount
            print("Withdrawal successful. Your new balance is:", balance)
    elif choice == '3':
        print("Your current balance is:", balance)
    elif choice == '4':
        print("Thank you for using our banking system.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")