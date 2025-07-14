import random
import string

def generate_password(length):
    letters = string.ascii_letters 
    digits = string.digits       
    symbols = string.punctuation    

    all_chars = letters + digits + symbols

    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    password += random.choices(all_chars, k=length - 3)

    random.shuffle(password)

    return ''.join(password)

try:
    length = int(input("Enter the desired password length: "))
    if length < 3:
        print("Password length must be at least 3 to include letters, digits, and symbols.")
    else:
        print("Generated Password:", generate_password(length))
except ValueError:
    print("Please enter a valid number.")
