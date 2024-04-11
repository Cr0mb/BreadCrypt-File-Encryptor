# Breadcrypt
Breadcrpyt is a Python script designed for file encryption and decryption using AES encryption. 
It allows users to encrypt and decrypt files using a passphrase. 
The script utilizes the cryptography library for cryptographic operations and provides a command-line interface for easy usage.

### Features
- Encryption: Encrypt files using AES encryption with a user-provided passphrase.
- Decryption: Decrypt encrypted files using the same passphrase used for encryption.
- Secure Key Derivation: Derives a secure key from the passphrase using PBKDF2 with SHA256.
- Command-Line Interface: Simple command-line interface for encrypting and decrypting files.
### Prerequisites
Before running the script, ensure you have the following dependencies installed:

- Python 3.x
- cryptography
- pyfiglet
- colorama

You can install the dependencies using pip:
```
pip install cryptography pyfiglet colorama
```
### Usage
1. Clone this repository to your local machine:
```
git clone https://github.com/Cr0mb/BreadCrypt-File-Encryptor.git
```
2. Navigate to the directory where you cloned the repository:
```
cd BreadCrypt-File-Encryptor
```
3. Run the script with appropriate options:
```
python encrypt.py [-e | -d] [-p FILE_PATH] [PASSWORD]

-e or --encrypt: Encrypt the file.
-d or --decrypt: Decrypt the file.
-p or --file_path: File path to be encrypted/decrypted.
PASSWORD: User-provided passphrase.

// If options are not provided, the script will prompt for necessary information interactively.
```

Created by Cr0mb.
