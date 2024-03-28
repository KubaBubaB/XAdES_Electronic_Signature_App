import os
import hashlib
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad


class RSAKeyGenerator:
    """
    A class used to generate and manage RSA keys.


    Attributes
    ----------
    pin : str
        a string used as a password to encrypt the private key
    private_key : bytes
        the private RSA key
    public_key : bytes
        the public RSA key

    Methods
    -------
    generate_keys():
        Generates a pair of RSA keys.
    save_keys():
        Saves the keys to files. The private key is encrypted.
    encrypt_private_key():
        Encrypts the private key using AES in CBC mode.
    """

    def __init__(self, pin):
        """
        Constructs all the necessary attributes for the RSAKeyGenerator object.

        Parameters
        ----------
            pin : str
                a string used as a password to encrypt the private key
        """
        self.pin = pin
        self.private_key = None
        self.public_key = None

    def generate_keys(self):
        """
        Generates a pair of RSA keys.
        """
        key = RSA.generate(4096)
        self.private_key = key.export_key()
        self.public_key = key.publickey().export_key()

    def save_keys(self):
        """
        Saves the keys to files. The private key is encrypted.
        """
        with open('private.pem', 'wb') as f:
            f.write(self.encrypt_private_key())

        with open('public.pem', 'wb') as f:
            f.write(self.public_key)

    def encrypt_private_key(self):
        """
        Encrypts the private key using AES in CBC mode.

        Returns
        -------
        bytes
            the encrypted private key concatenated with the initialization vector
        """
        key = hashlib.sha256(self.pin.encode()).digest()
        # init vector
        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        # pad the private key to 16 bytes, so it can be encrypted
        ciphertext = cipher.encrypt(pad(self.private_key, AES.block_size))
        return iv + ciphertext