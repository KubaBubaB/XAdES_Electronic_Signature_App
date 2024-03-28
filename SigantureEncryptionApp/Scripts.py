import os
import psutil
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import AES, PKCS1_OAEP
from Cryptodome.Util.Padding import unpad
import hashlib


def check_external_storage():
    """
    Checks if there is any external storage connected to the system.

    Returns
    -------
    str
        The mount point of the external storage if found, None otherwise.
    """
    partitions = psutil.disk_partitions(all=True)

    for partition in partitions:
        if partition.opts == 'rw,removable':
            return partition.mountpoint

    return None


def find_pem_files(root):
    """
    Finds all .pem files in the given root directory.

    Parameters
    ----------
    root : str
        The root directory to start the search from.

    Returns
    -------
    list
        A list of paths to the found .pem files. If no .pem files are found, returns None.
    """
    pems = []
    for dirpath, dirnames, filenames in os.walk(root):
        for filename in filenames:
            if filename.endswith(".pem"):
                pems.append(dirpath + "" + filename)

    if len(pems) == 0:
        return None
    return pems


def decrypt_RSA_key(pin, pem):
    """
    Decrypts the RSA key.

    Parameters
    ----------
    pin : str
        The pin used to encrypt the key.
    pem : str
        The path to the .pem file containing the encrypted key.

    Returns
    -------
    RSA key
        The decrypted RSA key.
    """
    # Read the encrypted private key from the file
    with open(pem, 'rb') as f:
        encrypted_key = f.read()

    # Extract the IV and the encrypted key
    iv = encrypted_key[:AES.block_size]
    encrypted_key = encrypted_key[AES.block_size:]

    # Generate the AES key from the PIN
    key = hashlib.sha256(pin.encode()).digest()

    # Create a new AES cipher
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the encrypted key
    decrypted_key = cipher.decrypt(encrypted_key)

    # Unpad the decrypted key
    private_key = unpad(decrypted_key, AES.block_size)

    # Return the RSA key
    return RSA.import_key(private_key)