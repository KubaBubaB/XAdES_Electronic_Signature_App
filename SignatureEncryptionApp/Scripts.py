import base64
import hashlib
import os
import psutil

from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import AES, PKCS1_OAEP
from Cryptodome.Signature import PKCS1_v1_5
from Cryptodome.Hash import SHA256
from Cryptodome.Util.Padding import unpad
from datetime import datetime
from uuid import getnode as get_mac
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, tostring, indent

ALLOWED_EXTENSIONS = ["cpp", "txt"]


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
                pems.append(os.path.join(dirpath, filename))

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


def is_file_valid_to_sign(file_name):
    """
    Checks if file has valid extension.

    Parameters
    ----------
    file_name : str
        The name of file with full path.

    Returns
    -------
    is_file_extension_valid : bool
    """
    file_extension = file_name.split(".")[-1].lower()
    is_file_extension_valid = file_extension in ALLOWED_EXTENSIONS

    return is_file_extension_valid


def sign_file(file_path, rsa_key):
    """
    Function creates new signature for file (file_path) using rsa_key.
    Signature contains:
        -file size,
        -file extension,
        -file modification date,
        -user name,
        -user MAC address,
        -file hash encrypted using rsa_key,
        -timestamp of signature,
    Signature is being saved in file "signature-{file_name}.xml"

    Parameters
    ----------
    file_name : str
        The name of file with full path.
    rsa_key : any
        Decrypted private key used to create hash of the document.

    Returns
    -------
    signature : str
        The XML of signature file.
    """
    with open(file_path, "rb") as file:
        file_content = file.read()

    # calculating hash of file
    file_hash = SHA256.new(file_content)

    # encrypting hash with decrypted private RSA key
    signer = PKCS1_v1_5.new(rsa_key)
    signature = signer.sign(file_hash)

    # creating XML signature
    signature_xml = Element("XAdES")

    file_info = SubElement(signature_xml, "FileInfo")
    SubElement(file_info, "Size").text = str(os.path.getsize(file_path))
    SubElement(file_info, "Extension").text = file_path.split(".")[-1]
    SubElement(file_info, "ModificationDate").text = str(datetime.fromtimestamp(os.path.getmtime(file_path)))

    user_info = SubElement(file_info, "UserInfo")
    SubElement(user_info, "SigningUserName").text = str(os.getlogin())
    SubElement(user_info, "SigningUserMAC").text = str(hex(get_mac()))

    SubElement(signature_xml, "EncryptedHash").text = base64.b64encode(signature).decode()
    SubElement(signature_xml, "Timestamp").text = str(datetime.now())

    indent(signature_xml, space='\t', level=0)
    signature_xml_str = tostring(signature_xml, encoding="unicode")

    # saving new signature
    signature_file_name = "signature-" + os.path.splitext(os.path.basename(file_path))[0] + ".xml"
    with open(signature_file_name, "w") as xml_file:
        xml_file.write(signature_xml_str)

    return signature_xml_str


def verify_signature(file_path, public_key_path, signature_path):
    """
    Function verifies the signature of the file.

    Parameters
    ----------
    file_path : str
        The path to the file to verify.
    signature_path : str
        The path to the signature file.
    public_key_path : str
        The path to the public key file.

    Returns
    -------
    bool
        True if the signature is valid, False otherwise.
    """
    with open(file_path, "rb") as file:
        file_content = file.read()

    # calculating hash of file
    file_hash = SHA256.new(file_content)

    # reading signature
    with open(signature_path, "r") as signature_file:
        signature_xml = signature_file.read()

    # parsing XML signature
    signature_tree = ElementTree.fromstring(signature_xml)

    with open(public_key_path, 'r') as key_file:
        public_key = RSA.import_key(key_file.read())

    # decrypting hash
    signature = base64.b64decode(signature_tree.find("EncryptedHash").text)

    # create a new verifier with the public key
    verifier = PKCS1_v1_5.new(public_key)

    # verify the signature
    is_signature_valid = verifier.verify(file_hash, signature)
    print(f"Is signature valid: {is_signature_valid}")

    return is_signature_valid


def encrypt_file(filePath, keyPath):
    """
    Function encrypts file (filePath) using key (keyPath) and replaces the original content with the encrypted content.

        Parameters
        ----------
        filePath : str
            The path to file to be encrypted.
        keyPath : str
            The path to public RSA key.

        Returns
        -------
        encrypted_content : str
            The string of encrypted file content.
    """

    with open(filePath, "rb") as file:
        fileContent = file.read()

    with open(keyPath, "r") as keyFile:
        publicKey = RSA.import_key(keyFile.read())

    # encrypt file content
    cipher = PKCS1_OAEP.new(publicKey)
    encrypted_content = cipher.encrypt(fileContent)

    # replace original content
    with open(filePath, "wb") as file:
        file.write(encrypted_content)

    return encrypted_content


def decrypt_file(filePath, key):
    """
    Function decrypts file (filePath) using the key.

        Parameters
        ----------
        filePath : str
            The path to encrypted file
        key : RSA_key
            Private RSA key.

        Returns
        -------
        decrypted_content : str
            The string of file content after decryption.
    """

    with open(filePath, "rb") as file:
        fileContent = file.read()

    cipher = PKCS1_OAEP.new(key)
    decrypted_content = cipher.decrypt(fileContent)

    decrypted_string = decrypted_content.decode('utf-8')
    with open(filePath, "wb") as file:
        file.write(decrypted_content)
    return decrypted_string
