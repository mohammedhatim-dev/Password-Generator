import random

print("--- Simple Password Generator ---")

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+"
all_characters = letters + numbers + symbols

try:
    length = int(input("Enter the desired password length: "))
    
    if length < 4:
        print("Security Warning: Password length should be at least 4 characters.")
    else:
        password = "".join(random.choice(all_characters) for _ in range(length))
        print(f"Your Generated Password is: {password}")

except ValueError:
    print("Error: Please enter a valid number for length.")