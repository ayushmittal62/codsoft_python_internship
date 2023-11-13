#random password generator 
import random
import string

def generate_password(length, use_uppercase, use_digits, use_special_chars):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase    
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        return "Cannot generate a password with no character set selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("Specify password criteria:")
    try:
        password_length = int(input("Password length: "))
        use_uppercase = input("Include uppercase letters (yes/no): ").strip().lower() == 'yes'
        use_digits = input("Include digits (yes/no): ").strip().lower() == 'yes'
        use_special_chars = input("Include special characters (yes/no): ").strip().lower() == 'yes'

        password = generate_password(password_length, use_uppercase, use_digits, use_special_chars)
        if password:
            print("Generated Password:", password)
        else:
            print("No character set selected. Cannot generate a password.")
    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")

if __name__ == "__main__":
    main()
