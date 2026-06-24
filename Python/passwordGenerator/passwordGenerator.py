userInput = input("Enter the length of the password: ")
# password generator
import random
import string
def generate_password(length):
    if length < 8:
        print("Password is too short. It should be at least 8 characters long.")
        return None
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

password = generate_password(int(userInput))
if password:
    print("Generated password:", password)  
    