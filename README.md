
## 🧪 Ransomware Simulation

> ⚠️ **Warning**  
> This project is strictly for **educational and research purposes** only.  
> Do not use this project for malicious activity.  
> The author is not responsible for any misuse.

This repository contains a ransomware simulation project developed as part of the **Santander Cybersecurity Bootcamp**.  
It demonstrates how ransomware encrypts and decrypts files using a combination of **RSA** and **AES** encryption methods.  
The goal is to understand cryptographic techniques and their potential misuse through hands-on learning.

---

## 🛡️ Project Overview

This project simulates the core behavior of a ransomware attack in a controlled, educational environment.  
It includes scripts for encrypting and decrypting files, showing how symmetric (AES) and asymmetric (RSA) encryption can be used together.

- `encrypter.py`: Encrypts files using AES and wraps the AES key with RSA
- `decrypter.py`: Decrypts the AES key with RSA and restores original files

---

## 🚀 Features

- **RSA Key Generation**  
  Automatically creates RSA 2048-bit public/private key pairs.

- **AES-256 File Encryption**  
  Encrypts file contents with AES; the AES key is then encrypted using RSA.

- **Secure Decryption Process**  
  Decrypts the AES key with the private RSA key and uses it to recover file contents.

- **Directory Management**  
  Organizes original, encrypted, and decrypted files in dedicated folders.

---

## ⚙️ Requirements

- Python 3.8 or higher
- Python package: `cryptography`

### Install Dependencies

```bash
pip install cryptography
```

---

## 🛠️ Technologies Used

- **Language**: Python 3  
- **Library**: [cryptography](https://cryptography.io/en/latest/)  
- **Encryption Methods**:
  - **AES-256** (CBC mode) for file content
  - **RSA-2048** for encrypting the AES key

---

## 📚 Ethics

This project was created solely for **educational and ethical purposes**.  
It must **not** be used in real-world attacks or for unauthorized activities under any circumstances.

By using or referencing this code, you agree to:

- Use it only in **controlled lab environments**
- Respect all **legal and ethical standards**
- Never use it to harm individuals, systems, or organizations

The author is **not responsible** for any misuse or illegal application of this code.
