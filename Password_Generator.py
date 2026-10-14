
import random
import string

print("=" * 40)
print("       🔐 PASSWORD GENERATOR 🔐")
print("=" * 40)

try:
    length = int(input("👉 Enter password length: "))

    if length <= 0:
        print("❌ Please enter a positive number.")

    else:
        letters = string.ascii_letters
        numbers = string.digits
        symbols = "!@#$%&*"

        characters = letters + numbers + symbols

        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("\n" + "-" * 40)
        print("✅ PASSWORD GENERATED SUCCESSFULLY!")
        print("-" * 40)
        print(f"🔑 Your Password: {password}")
        print(f"📏 Password Length: {length}")
        print("-" * 40)
        print("🔒 Keep your password safe!")
        print("=" * 40)

except ValueError:
    print("❌ Invalid input! Please enter a number.")