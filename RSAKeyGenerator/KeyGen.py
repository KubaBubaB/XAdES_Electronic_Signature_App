import os
import hashlib
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

class RSAKeyGenerator:
    def __init__(self, pin):
        self.pin = pin
        self.private_key = None
        self.public_key = None

    def generate_keys(self):
        key = RSA.generate(4096)
        self.private_key = key.export_key()
        self.public_key = key.publickey().export_key()

    def save_keys(self):
        with open('private.pem', 'wb') as f:
            f.write(self.encrypt_private_key())

        with open('public.pem', 'wb') as f:
            f.write(self.public_key)

    def encrypt_private_key(self):
        key = hashlib.sha256(self.pin.encode()).digest()
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(self.private_key)
        return cipher.nonce + tag + ciphertext