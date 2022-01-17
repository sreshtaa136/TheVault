#!/usr/local/bin/python3

import os
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet, InvalidToken

# key = Fernet.generate_key()
# keyFile = "key.key"
# with open(keyFile, "wb") as f:
#     f.write(key) 

# To read the key
# with open(keyFile, "rb") as f:
#     key = f.read()

class Security:

    def generate_key(self, password_input):
        # password_input = input("Enter your password: ")
        password = password_input.encode() #Converting to type 'bytes'
        salt = b'Nwm\xb0\x9d=R\xaf-`\xeb\xc7\x94\xef\xf1\xbe\xdd\xa9\x93k\xda\xe6\xedk\x96\xa3\x1d\xfd\x85\x9f\x0c\xf1\xa2\xab\xed\xe4'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password)) 

        # keyFile = "key.key"

        # # To write the key
        # with open(keyFile, "wb") as f:
        #     f.write(key)
        return key


    # # To read the key
    # with open(keyFile, "rb") as f:
    #     key = f.read()

    def encrypt_file(self, key):
        # Opening the file to encrypt
        with open("Vault.txt", "rb") as f:
            data = f.read()

        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)

        # Writing encrypted data
        with open("Vault.encrypted", "wb") as f:
            f.write(encrypted)
        os.remove("Vault.txt")


    def decrypt_file(self, key):
        # Decrypt the file
        with open("Vault.encrypted", "rb") as f:
            data = f.read()

        fernet = Fernet(key)
        try:       
            decrypted = fernet.decrypt(data)
            # Writing decrypted data
            with open("Vault.txt", "wb") as f:
                f.write(decrypted)
            os.remove("Vault.encrypted")
        except InvalidToken as e:
            print("Invalid Key - Unsuccessful decryption")