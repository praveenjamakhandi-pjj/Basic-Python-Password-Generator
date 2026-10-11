
import random
import string

print("PASSWORD GENERATOR")

length = int(input("Enter password length: "))

if length <= 0:
    print("Please enter a positive number.")
else:
    letters = string.ascii_letters
    numbers = string.digits
    symbols = "!@#$%&*"

    characters = letters + numbers + symbols

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Your password is:", password)
