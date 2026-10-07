import random
import string

print("PASSWORD GENERATOR")

length = int(input("Enter password length: "))

letters = string.ascii_letters
numbers = string.digits
symbols = "!@#$%&*"

characters = letters + numbers + symbols

password = ""

for i in range(length):
    password = password + random.choice(characters)

print("Your password is:", password)