# 🔐 Secret Message Encryptor

A simple Python project that allows users to **encrypt and decrypt secret messages** using a custom **2-digit passcode**. The message can only be read by someone who knows the correct passcode.

This project demonstrates basic encryption concepts, user input handling, string manipulation, and SHA-256 passcode verification.

---

## ✨ Features

- 🔒 Encrypt secret messages
- 🔑 Create your own 2-digit passcode
- 🛡️ Passcode verification using SHA-256 hashing
- 🔓 Decrypt messages only with the correct passcode
- 📝 Preserves spaces, numbers, and special characters
- 💻 Simple menu-driven console application

---

## 📂 Project Structure

```
Secret-Message-Encryptor/
│── secret_message_encryptor.py
│── README.md
│── screenshots/
│     └── output.png
```

---

## 🚀 How It Works

### Encryption

1. Run the program.
2. Select **Encrypt Message**.
3. Enter your secret message.
4. Create a 2-digit passcode.
5. The program encrypts your message.
6. Share the encrypted message and passcode with your friend.

### Decryption

1. Run the program.
2. Select **Decrypt Message**.
3. Enter the encrypted message.
4. Enter the passcode hash.
5. Enter the correct passcode.
6. If the passcode matches, the original message is displayed.

---

## ▶️ How to Run

### Clone the repository

```bash
git clone https://github.com/yourusername/Secret-Message-Encryptor.git
```

### Open the project folder

```bash
cd Secret-Message-Encryptor
```

### Run the program

```bash
python secret_message_encryptor.py
```

---

## 💻 Sample Output

### Encrypt Message

```
==================================================
        SECRET MESSAGE ENCRYPTOR
==================================================

1. Encrypt Message
2. Decrypt Message
3. Exit

Choose an option (1-3): 1

Enter your secret message:
Meet me tomorrow at 7 PM

Create a 2-digit passcode (10-99): 25

==================================================
ENCRYPTED MESSAGE
==================================================
Jxxm fx mhfhkkhp tm 7 EB

Passcode Hash:
8e296a067a37563370ded05f5a3bf3ec...

Share this encrypted message and your passcode.
```

---

### Decrypt Message

```
Choose an option (1-3): 2

Enter encrypted message:
Jxxm fx mhfhkkhp tm 7 EB

Enter passcode hash:
8e296a067a37563370ded05f5a3bf3ec...

Enter passcode:
25

==================================================
ORIGINAL MESSAGE
==================================================
Meet me tomorrow at 7 PM
```

---

## 🛠️ Technologies Used

- Python 3
- hashlib (Built-in Library)

---

## 📚 Concepts Used

- Functions
- Loops
- Conditional Statements
- String Manipulation
- ASCII Values (`ord()` & `chr()`)
- SHA-256 Hashing
- User Input Validation

---

## 🎯 Learning Outcomes

By building this project, you will learn:

- Basic encryption techniques
- Password verification using hashing
- How Caesar Cipher works
- Python functions
- Error handling
- Menu-driven applications

---

## 🚀 Future Improvements

- 📂 Encrypt and decrypt text files
- 🖥️ GUI using Tkinter
- 🌐 Web version using Flask
- 🔐 AES/Fernet encryption for real security
- 📋 Copy encrypted message to clipboard
- 💾 Save encrypted messages automatically

---



## 👨‍💻 Author

**Simi Dubey**

Aspiring Data Scientist | Python | SQL | Power BI | Machine Learning

---

## ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub!
