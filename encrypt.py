"""
Author: Rob Dunsmuir
Date: Feburary 19, 2022
Purpose: Encrypt class, encrypts and decrypts textual data when reading/writing files 
Status: in Beta
"""

# pip install cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os


class Encryption:

    def __init__(self, passwd):
        self.password = passwd
        self.key = None
        self.generate_key()

    def generate_key(self):
        password_provided = self.password
        enc_password = password_provided.encode()
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=os.urandom(16),
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(enc_password))
        self.key = key

    def get_key(self):
        return self.key

    def encrypt_content(self, content):
        fernet = Fernet(self.key)
        content_as_bytes = bytes(content, 'utf-8')
        encrypted = fernet.encrypt(content_as_bytes)
        return encrypted

    def decrypt_content(self, content):
        fernet = Fernet(self.key)
        decrypted = str(fernet.decrypt(content))
        # remove first 2 and last char
        decrypted = decrypted[2:-1]
        return decrypted


# test code
if __name__ == "__main__":
    password = "abc123"
    enc = Encryption(password)
    print(f"key: {enc.get_key()}")
    my_content = "this is my alphabet abcdef"
    print(f"my_content: {my_content}")
    my_encrypted = enc.encrypt_content(my_content)
    print(f"encrypted: "+str(my_encrypted))
    my_decrypted = enc.decrypt_content(my_encrypted)
    print(f"decrypted: "+str(my_decrypted))

