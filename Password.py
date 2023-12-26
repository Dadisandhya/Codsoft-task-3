import random
import string

def generate_password(length=12, uppercase=True, digits=True, symbols=True):
    characters = string.ascii_letters if uppercase else string.ascii_lowercase
    characters += string.digits if digits else ''
    characters += string.punctuation if symbols else ''

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    # Get user input for password parameters
    length = int(input("Enter password length: "))
    uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    digits = input("Include digits? (yes/no): ").lower() == 'yes'
    symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

    # Generate and print the password
    password = generate_password(length, uppercase, digits, symbols)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
