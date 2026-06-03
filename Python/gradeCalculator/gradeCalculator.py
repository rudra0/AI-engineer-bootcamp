name = input("Enter your name: ")
grade = float(input("Enter your grade: "))
if grade >= 90:
    print(f"{name}, you got an A!")
elif grade >= 80:
    print(f"{name}, you got a B!")
elif grade >= 70:
    print(f"{name}, you got a C!")
elif grade >= 60:
    print(f"{name}, you got a D!")
else:    print(f"{name}, you got an F!")

# Case Conversion
# print(f"{name.upper()}, Name in Upper Case")
# print(f"{name.lower()}, Name in Lower Case")
# print(f"{name.capitalize()}, Name with First Letter Capitalized")