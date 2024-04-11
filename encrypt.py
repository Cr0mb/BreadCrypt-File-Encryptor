import os
import argparse
from getpass import getpass  
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
try:
    import pyfiglet
    from colorama import Fore, init
    init(autoreset=True)  
    
except ImportError:
    print("Required modules not found. Installing...")
    os.system("pip install pyfiglet colorama")
    import pyfiglet
    from colorama import Fore, init
    init(autoreset=True) 
def print_title():
    custom_fig = pyfiglet.Figlet(font='standard')
    title_text = custom_fig.renderText('Breadcrypt')
    print(Fore.LIGHTYELLOW_EX + title_text)
    
def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt_file(file_path, password, delete_original=False):
    salt = os.urandom(16)
    key = derive_key(password, salt)
    iv = os.urandom(16)


    with open(file_path, 'rb') as file:
        plaintext = file.read()
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    encrypted_file_path = file_path + ".enc"
    
    
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(salt + iv + ciphertext)
    if delete_original:
        os.remove(file_path)

def decrypt_file(encrypted_file_path, password):
    with open(encrypted_file_path, 'rb') as file:
        data = file.read()

    salt = data[:16]
    iv = data[16:32]
    ciphertext = data[32:]
    
    key = derive_key(password, salt)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    original_file_path = encrypted_file_path[:-4]
    
    with open(original_file_path, 'wb') as original_file:
        original_file.write(plaintext)

def main():
    parser = argparse.ArgumentParser(description='File Encryptor/Decryptor')
    parser.add_argument('-e', '--encrypt', action='store_true', help='Encrypt the file.')
    parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt the file.')
    parser.add_argument('-p', '--file_path', help='File path to be encrypted/decrypted. Include quotations for directory "C:\\"')
    parser.add_argument('password', nargs='?', help='User-provided passphrase.')
    args = parser.parse_args()

    if not any(vars(args).values()):
        print_title()
        args.encrypt = input('Do you want to encrypt the file? (y/n): ').lower() == 'y'
        args.decrypt = input('Do you want to decrypt the file? (y/n): ').lower() == 'y'
        args.file_path = input('Enter the file path: ')
        args.password = getpass('Enter the passphrase: ')

    if args.encrypt:
        encrypt_file(args.file_path, args.password, delete_original=True)
        print('Encryption successful.')
    elif args.decrypt:
        decrypt_file(args.file_path, args.password)
        print('Decryption successful.')

if __name__ == "__main__":
    main()
