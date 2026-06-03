for i in range(1,11):
    if i % 2 == 0:
        print(i, "is even")

# Multiplication table 
num = int(input("Enter a number to see its multiplication table: " ))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
