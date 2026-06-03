USD = float(input("Enter amount in USD: "))
print("Select currency to convert to:")
print("1. INR")
print("2. EUR")
print("3. GBP")
choice = input("Enter choice(1/2/3): ")
if choice == '1':
  print(USD, "USD is equal to", USD * 96.0, "INR")
elif choice == '2':
  print(USD, "USD is equal to", USD * 0.85, "EUR")
elif choice == '3':
  print(USD, "USD is equal to", USD * 0.75, "GBP")
else:  print("Invalid input") 