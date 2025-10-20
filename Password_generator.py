# password_generator.py
import random
import string

def generate_password(length, use_digits=True, use_symbols=True):
    # Start with letters
    characters = list(string.ascii_letters)

    # Add digits if chosen
    if use_digits:
        characters += list(string.digits)

    # Add punctuation symbols if chosen
    if use_symbols:
        characters += list(string.punctuation)

    # Check for minimum length
    if length < 4:
        print("Password length too short! Use at least 4 characters.")
        return None

    # Generate password using random.choice
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("\n--- PASSWORD GENERATOR ---")
    try:
        length = int(input("Enter desired password length: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_digits, use_symbols)

    if password:
        print("\n✅ Your generated password is:")
        print(password)
        print("\nKeep it safe & secure!")

if __name__ == "__main__":
    main()