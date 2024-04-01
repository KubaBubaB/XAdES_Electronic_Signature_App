import customtkinter as ctk
import Frames as fr
import Scripts as Scripts

class AppController(ctk.CTk):
    """
    A class used to control the application.

    Attributes
    ----------
    width_ : int
        The width of the application window.
    height_ : int
        The height of the application window.
    current_ : any
        The current frame of the application.
    frames_ : dict
        A dictionary to store the frames of the application.
    text_ : str
        A string to store text.

    Methods
    -------
    __init__():
        Initializes the application.
    sign_document_choosen():
        Checks if there is any external storage connected to the system and finds .pem files.
    set_frame(frame_name: any, *args):
        Sets the current frame of the application.
    encrypt_key(name: str):
        Prints the name of the key.
    handle_pin_entry(pin: str, path: str):
        Handles the pin entry.
    select_file_to_sign():
        Handles selecting file to sign.
    """

    width_ = 800
    height_ = 600
    current_ = None
    frames_ = {}
    text_ = ""

    def __init__(self):
        """
        Constructs all the necessary attributes for the AppController object.
        """
        super().__init__()

        self.title("Singature Encryption App")
        self.geometry(f"{self.width_}x{self.height_}")
        self.resizable(False, False)
        ctk.set_appearance_mode("Dark")
        self.set_frame(fr.HomeFrame)
        self.rsa_key = None

    def sign_document_choosen(self):
        """
        Checks if there is any external storage connected to the system and finds .pem files.
        If storage is found, sets the FoundPendriveFrame as the current frame.
        If no storage is found, sets the NoPendriveFrame as the current frame.
        """
        storage = Scripts.check_external_storage()
        if storage is not None:
            pems = Scripts.find_pem_files(storage)
            self.set_frame(fr.FoundPendriveFrame, storage, pems)
        else:
            self.set_frame(fr.NoPendriveFrame)

    def set_frame(self, frame_name, *args):
        """
        Sets the current frame of the application.

        Parameters
        ----------
            frame_name : any
                The name of the frame to be set as the current frame.
            *args : list
                The arguments to be passed to the frame constructor.
        """
        if self.current_ is not None:
            self.current_.pack_forget()
        self.current_ = frame_name(self, self, *args)
        self.current_.pack(expand=True, fill="both")

    def decrypt_key(self, path):
        """
        Switches frame to pin entering.

        Parameters
        ----------
            path : str
                Path to the key.
        """
        self.set_frame(fr.PinEntryFrame, path, False, True, None)

    def handle_pin_entry(self, pin, path, isKeyForSignature, fileToDecryptPath):
        """
        Handles the pin entry.
        If key is correct, sets the SelectFileToSignFrame as the current frame.
        If isn't correct, sets the PinEntryFrame with flag signalising wrong pin as the current frame.

        Parameters
        ----------
            pin : str
                The pin used to encrypt the key.
            path : str
                Path to the key.
            isKeyForSignature : bool
                A flag to signalise if the key is for signature.
            fileToDecryptPath : str
                Path to the file to decrypt.
        """
        try:
            key = Scripts.decrypt_RSA_key(pin, path)
            if key is not None:
                print(key.export_key().decode())
                self.rsa_key = key
                self.text_ = key
                if isKeyForSignature:
                    self.set_frame(fr.SelectFileToSignFrame, None, False)
                else:
                    self.decrypt_file(self.rsa_key, fileToDecryptPath)
            else:
                print("Error decrypting key")
                pass
        except ValueError:
            self.set_frame(fr.PinEntryFrame, path, True, isKeyForSignature, fileToDecryptPath)

    def select_file_to_sign(self):
        """
        Handles selecting file to sign
        If the extension of file is correct, sets SelectFileToSignFrame with adequate parameters:
            SelectFileToSignFrame(filePath=path, isExtensionValid=True)
        And if otherwise with arguments:
            SelectFileToSignFrame(filePath=path, isExtensionValid=False)
        """
        filename = ctk.filedialog.askopenfilename()

        isExtensionValid = Scripts.is_file_valid_to_sign(filename)
        self.set_frame(fr.SelectFileToSignFrame, filename, isExtensionValid)

    def select_file_to_verify(self):
        """
        Handles selecting file to verify
        If the extension of file is correct, sets SelectFileToVerifyFrame with adequate parameters:
            SelectFileToVerifyFrame(filePath=path, isExtensionValid=True)
        And if otherwise with arguments:
            SelectFileToVerifyFrame(filePath=path, isExtensionValid=False)
        """
        filename = ctk.filedialog.askopenfilename()

        isExtensionValid = Scripts.is_file_valid_to_sign(filename)
        self.set_frame(fr.SelectFileToVerifyFrame, filename, isExtensionValid)

    def verify_signature(self, file_path):
        """
        Starts to handle VERIFY operation.
        :param file_path:
        :return:
        """
        self.set_frame(fr.SelectPublicKeyFrame, file_path, None, None)

    def verify_signature2(self, file_path, public_key_path):
        """
        Continues to handle VERIFY operation.
        :param file_path:
        :param public_key_path:
        """
        self.set_frame(fr.SelectXMLFrame, file_path, public_key_path, None, None)

    def verify_signature3(self, file_path, public_key_path, signature_path):
        """
        Finishes handling VERIFY operation.

        Parameters
        ----------
            file_path : str
                The path to the file to verify.
            public_key_path : str
                The path to the public key file.
            signature_path : str
                The path to the signature file.
        """
        result = Scripts.verify_signature(file_path, public_key_path, signature_path)
        # print(result)
        self.set_frame(fr.VerificationResultFrame, result)

    def select_public_key(self, filepath):
        """
        Handles selecting public key.
        If the extension of file is correct, sets SelectPublicKeyFrame with adequate parameters:
            SelectPublicKeyFrame(filePath=path, isExtensionValid=True)
        And if otherwise with arguments:
            SelectPublicKeyFrame(filePath=path, isExtensionValid=False)

        Parameters
        ----------
            filepath : str
                The path to the file.
        """
        keyname = ctk.filedialog.askopenfilename()

        isExtensionValid = (keyname.split(".")[-1].lower() == "pem")
        self.set_frame(fr.SelectPublicKeyFrame, filepath, isExtensionValid, keyname)

    def select_signature(self, file_path, public_key_path):
        """
        Handles selecting signature.
        If the extension of file is correct, sets SelectSignatureFrame with adequate parameters:
            SelectSignatureFrame(filePath=path, isExtensionValid=True)
        And if otherwise with arguments:
            SelectSignatureFrame(filePath=path, isExtensionValid=False)

        Parameters
        ----------
            file_path : str
                The path to the file.
            public_key_path : str
                The path to the public key file.
        """
        signature = ctk.filedialog.askopenfilename()

        isExtensionValid = (signature.split(".")[-1].lower() == "xml")
        self.set_frame(fr.SelectXMLFrame, file_path, public_key_path, isExtensionValid, signature)

    def sign_the_file(self, file_path):
        """
        Handles SIGN operation.
        :param file_path:
        """
        signature = Scripts.sign_file(file_path, self.rsa_key)
        self.set_frame(fr.SuccessfulOperationWithDisplay, "SIGNATURE COMPLETED", signature)


    def select_encrypt_decrypt(self):
        """
        Method sets SelectEncryptDecryptFrame with default parameters
        """
        self.set_frame(fr.SelectEncryptDecryptFrame)

    def selected_encrypt(self):
        """
        Method sets SelectFileToEncryptFrame with default parameters
        """
        self.set_frame(fr.SelectFileToEncryptFrame, None, False)

    def select_file_to_encrypt(self):
        """
        Method handles selecting file to be encrypted.
        It also cheks if file has allowed extension and propagate it to SelectFileToEncryptFrame
        """
        filepath = ctk.filedialog.askopenfilename()

        isExtensionValid = Scripts.is_file_valid_to_sign(filepath)
        self.set_frame(fr.SelectFileToEncryptFrame, filepath, isExtensionValid)

    def selected_file_to_encrypt(self, filepath):
        """
        Method sets SelectPublicKeyToEncryptFrame with default parameters

        Parameters
        ----------
            filepath : str
        """
        self.set_frame(fr.SelectPublicKeyToEncryptFrame, filepath, None, False)

    def select_public_key_to_encrypt(self, filepath):
        """
        Method handles selecting key to sign previously selected file.
        It also cheks if file has allowed extension and propagate it to SelectPublicKeyToEncryptFrame

        Parameters
        ----------
            filepath : str
        """
        keyPath = ctk.filedialog.askopenfilename()

        isExtensionValid = (keyPath.split(".")[-1].lower() == "pem")
        self.set_frame(fr.SelectPublicKeyToEncryptFrame, filepath, keyPath, isExtensionValid)

    def selected_decrypt(self):
        """
        Method sets SelectFileToDecryptFrame with default parameters
        """
        self.set_frame(fr.SelectFileToDecryptFrame, None, False)

    def select_file_to_decrypt(self):
        """
        Method handles selecting file to be signed.
        It also cheks if file has allowed extension and propagate it to SelectFileToDecryptFrame
        """
        filepath = ctk.filedialog.askopenfilename()

        isExtensionValid = Scripts.is_file_valid_to_sign(filepath)
        self.set_frame(fr.SelectFileToDecryptFrame, filepath, isExtensionValid)

    def selected_file_to_decrypt(self, filePath):
        """
        Checks if there is any external storage connected to the system and finds .pem files.
        If storage is found, sets the FoundPendriveForDecryptionFrame as the current frame.
        If no storage is found, sets the NoPendriveForDecryptionFrame as the current frame.

        Parameters
        ----------
            filePath : str
        """
        storage = Scripts.check_external_storage()
        if storage is not None:
            pems = Scripts.find_pem_files(storage)
            self.set_frame(fr.FoundPendriveForDecryptionFrame, storage, pems, filePath)
        else:
            self.set_frame(fr.NoPendriveForDecryptionFrame, filePath)

    def selected_decrypt_key_for_file_decryption(self, keyPath, filePath):
        """
        Switches frame to pin entering with filePath parameter.

        Parameters
        ----------
            keyPath : str
                Path to the key.
            filePath : str
                Path to the file.
        """
        self.set_frame(fr.PinEntryFrame, keyPath, False, False, filePath)

    def encrypt_file(self, filePath, keyPath):
        """
        Method takes file and key paths and calls method Scripts.encrypt_file(),
        then takes value of encrypted file and propagate it to be shown on SuccessfulOperationWithDisplay

        Parameters
        ----------
            filePath : str
            keyPath : str
        """
        encrypted_file = Scripts.encrypt_file(filePath, keyPath)
        self.set_frame(fr.SuccessfulOperationWithDisplay, "FILE ENCRYPTION COMPLETED", encrypted_file)

    def decrypt_file(self, key, filePath):
        """
        Method takes file path and RSA key and calls method Scripts.decrypt_file(),
        then takes value of decrypted file and propagate it to be shown on SuccessfulOperationWithDisplay

        Parameters
        ----------
            key : RSA key
            filePath : str
        """
        decrypted_file = Scripts.decrypt_file(filePath, key)
        self.set_frame(fr.SuccessfulOperationWithDisplay, "FILE DECRYPTION COMPLETED", decrypted_file)