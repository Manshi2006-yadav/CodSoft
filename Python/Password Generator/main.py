from generator import generate_password

print("PASSWORD GENERATOR")

try:
    length = int(input("Enter password length: "))

    if length <= 0:
        print("Length must be greater than 0")
    else:
        password = generate_password(length)

        print("\nGenerated Password:")
        print(password)

except ValueError:
    print("Please enter a valid number.")