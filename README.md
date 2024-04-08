
# XAdES_Electronic_Signature_App

This application uses RSA and AES algorithms is designed to implement the XAdES electronic signature standard. It is developed in Python and consists of two main parts:


## RSAKeyGenerator

This console application is responsible for generating private and public key. It emulates Trusted Third Party (TTP). Private key is generated with custom PIN.
## SignatureEncryptionApp
This application uses RSA algorithm and provides the following functionalities to SMALL .txt or .cpp files:
- Signing a document with the private key, after providing the correct PIN
- Verify a signature with the public key
- Encryption of a small document with the public key
- Decryption of a document with the private key and a PIN## Run Locally

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Steps

1. Clone the repository:
   ```
   git clone https://github.com/KubaBubaB/XAdES_Electronic_Signature_App
   ```

2. Navigate to the project directory:
   ```
   cd XAdES_Electronic_Signature_App
   ```

3. It's recommended to create a virtual environment to isolate the project dependencies. You can do this using the following commands:
   ```
   python -m venv venv
   source venv/bin/activate  
   # On Windows, use `venv\Scripts\activate`
   ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Now you can run applications.
---
Please note that this is a basic Python project setup. Depending on the specific requirements and dependencies of your project, additional steps may be necessary.
---
## Usage / Examples 

### RSAKeyGenerator
Generating a pair of keys
1. Run the app.
2. Type
```
generate
```
3. Type chosen PIN number (ie. 1234)
```
1234
```
4. Keys should generate in the project folder in the .pem format

### SignatureEncryptionApp
Signing a file
1. Make sure that a private key is stored on the external storage
2. Choose the private key
3. Enter the PIN that was used to encrypt the private key
4. Select a file to sign
5. The signature should be created in the following standard:
 - Signature contains:
    - file's size,
    - file's extension,
    - file's modification date,
    - user's name,
    - user's MAC address,
    - file's hash encrypted using rsa_key,
    - timestamp of the signature,
 - Signature is saved in the "signature-{file_name}.xml" file
 ---
Verifying a Signature

1. Select the file to be verified
2. Select the public key
3. Select the signature
4. The result of the verification is displayed
---
Encrypting a file

1. Select a file to encrypt
2. Select a public key
3. The file is now encrypted 
---
Decrypting a file

1. Select a file to decrypt 
2. Select a private key
3. Enter the PIN
4. File is now decrypted


## Authors

- [@Aleksander Sarzyniak](https://www.https://github.com/alexander0077)
- [@Kuba Lisowski](https://www.https://github.com/KubaBubaB)

