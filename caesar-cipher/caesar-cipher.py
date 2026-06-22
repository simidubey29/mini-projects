# ==========================================
# Caesar Cipher Encryption & Decryption
# Author: Simi Dubey
# ==========================================

def encrypt(text, shift):
    encrypted = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - start + shift) % 26 + start)
        else:
            encrypted += char

    return encrypted


def decrypt(text, shift):
    return encrypt(text, -shift)


def main():
    print("=" * 45)
    print("     CAESAR CIPHER ENCRYPTION TOOL")
    print("=" * 45)

    while True:
        print("\nChoose an option:")
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ")

        if choice == "1":
            text = input("\nEnter text to encrypt: ")
            shift = int(input("Enter shift value: "))

            encrypted = encrypt(text, shift)

            print("\nEncrypted Text:")
            print(encrypted)

        elif choice == "2":
            text = input("\nEnter text to decrypt: ")
            shift = int(input("Enter shift value: "))

            decrypted = decrypt(text, shift)

            print("\nDecrypted Text:")
            print(decrypted)

        elif choice == "3":
            print("\nThank you for using Caesar Cipher!")
            break

        else:
            print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    main()
