# ==========================================
# Secret Message Encryptor
# Author: Simi Dubey
# ==========================================

import hashlib


def encrypt(message, key):
    encrypted = ""

    for char in message:
        if char.isalpha():
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            encrypted += chr((ord(char) - start + key) % 26 + start)

        else:
            encrypted += char

    return encrypted


def decrypt(message, key):
    decrypted = ""

    for char in message:
        if char.isalpha():
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            decrypted += chr((ord(char) - start - key) % 26 + start)

        else:
            decrypted += char

    return decrypted


print("=" * 50)
print("        SECRET MESSAGE ENCRYPTOR")
print("=" * 50)

while True:

    print("\n1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Exit")

    choice = input("\nChoose an option (1-3): ")

    if choice == "1":

        message = input("\nEnter your secret message:\n")

        while True:
            passcode = input("Create a 2-digit passcode (10-99): ")

            if passcode.isdigit() and 10 <= int(passcode) <= 99:
                break
            else:
                print("Invalid passcode! Enter only a 2-digit number.")

        key = int(passcode)

        encrypted = encrypt(message, key)

        password_hash = hashlib.sha256(passcode.encode()).hexdigest()

        print("\n" + "=" * 50)
        print("ENCRYPTED MESSAGE")
        print("=" * 50)
        print(encrypted)

        print("\nPasscode Hash (used for verification)")
        print(password_hash)

        print("\nShare ONLY:")
        print("1. Encrypted Message")
        print("2. Your Passcode")
        print("=" * 50)

    elif choice == "2":

        encrypted_message = input("\nEnter encrypted message:\n")

        saved_hash = input("\nEnter passcode hash:\n")

        entered_passcode = input("Enter passcode: ")

        entered_hash = hashlib.sha256(entered_passcode.encode()).hexdigest()

        if entered_hash == saved_hash:

            decrypted = decrypt(encrypted_message, int(entered_passcode))

            print("\n" + "=" * 50)
            print("ORIGINAL MESSAGE")
            print("=" * 50)
            print(decrypted)

        else:
            print("\n❌ Wrong Passcode!")
            print("Access Denied.")

    elif choice == "3":
        print("\nThank you for using Secret Message Encryptor!")
        break

    else:
        print("\nInvalid choice. Try again.")
