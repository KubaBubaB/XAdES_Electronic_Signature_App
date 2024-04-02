import os.path

import customtkinter as ctk
from PIL import Image, ImageTk

additional_path = '/icons'
if not os.path.exists(additional_path):
    additional_path = 'SignatureEncryptionApp' + additional_path


class HomeFrame(ctk.CTkFrame):
    """
    A class used to represent the Home Frame of the application.


    Methods
    -------
    __init__(master: any, appController):
        Initializes the Home Frame with buttons for different functionalities.
    """

    def __init__(self, master: any, appController):
        """
        Constructs all the necessary attributes for the HomeFrame object.

        Parameters
        ----------
            master : any
                The parent widget.
            appController : any
                The application controller.
        """
        super().__init__(master)

        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure((1, 2, 3, 4), weight=1)
        self.grid_rowconfigure(5, weight=2)
        self.grid_columnconfigure((0, 1), weight=1)

        label = ctk.CTkLabel(master=self, text="SIGNATURE ENCRYPTION \n APP", font=("Georgia", 50))
        label.grid(row=0, column=0, columnspan=2)

        sign_button = ctk.CTkButton(self, text="Sign the document", font=("Calibri", 40), width=400, height=60,
                                    command=lambda: appController.sign_document_choosen())
        sign_button.grid(row=1, column=0, padx=10, pady=1)

        validate_button = ctk.CTkButton(self, text="Verify signature", font=("Calibri", 40), width=400, height=60,
                                        command=lambda: appController.set_frame(SelectFileToVerifyFrame, None, None))
        validate_button.grid(row=2, column=0, padx=10, pady=1)

        encrypt_button = ctk.CTkButton(self, text="Encryption/decryption", font=("Calibri", 40), width=400, height=60,
                                       command=lambda: appController.select_encrypt_decrypt())
        encrypt_button.grid(row=3, column=0, padx=10, pady=1)

        about_button = ctk.CTkButton(self, text="About app", font=("Calibri", 40), width=400, height=60,
                                     command=lambda: appController.set_frame(AboutFrame))
        about_button.grid(row=4, column=0, padx=10, pady=1)

        img = None
        img = ctk.CTkImage(Image.open(additional_path + "/certificate.png"), size=(300, 300))
        label = ctk.CTkLabel(master=self, image=img, text="")
        label.grid(row=1, column=1, rowspan=4)


class AboutFrame(ctk.CTkFrame):
    """
    A class used to represent the About Frame of the application.


    Methods
    -------
    __init__(master: any, appController):
        Initializes the About Frame with information about the application.
    """

    def __init__(self, master: any, appController):
        """
        Constructs all the necessary attributes for the AboutFrame object.

        Parameters
        ----------
            master : any
                The parent widget.
            appController : any
                The application controller.
        """
        super().__init__(master)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure((1, 2, 3, 4, 5), weight=2)
        self.grid_rowconfigure(6, weight=1)
        self.grid_columnconfigure(0, weight=1)

        label = ctk.CTkLabel(master=self, text="ABOUT APP", font=("Georgia", 50))
        label.grid(row=0, column=0, pady=20)

        text = "This application allows you to sign and verify documents. " \
               "It also provides the option to encrypt and decrypt files. " \
               "The application uses RSA encryption algorithm.\n" \
               "Authors: \n" \
               "Aleksander Sarzyniak \n" \
               "Kuba Lisowski \n"

        text_label = ctk.CTkLabel(master=self, text=text, font=("Calibri", 30), wraplength=750)
        text_label.grid(row=1, column=0, pady=20)

        return_button = ctk.CTkButton(self, text="Return to main menu", font=("Calibri", 30), width=300, height=50,
                                      command=lambda: appController.set_frame(HomeFrame))
        return_button.grid(row=6, column=0, padx=10, pady=10)


class NoPendriveFrame(ctk.CTkFrame):
    """
    A class used to represent the No Pendrive Frame of the application.

    Methods
    -------
    __init__(master: any, appController):
        Initializes the No Pendrive Frame with a message and buttons for retry and return to main menu.
    """

    def __init__(self, master: any, appController):
        """
        Constructs all the necessary attributes for the NoPendriveFrame object.

        Parameters
        ----------
            master : any
                The parent widget.
            appController : any
                The application controller.
        """
        super().__init__(master)

        self.grid_rowconfigure(1, weight=9)
        self.grid_rowconfigure((0, 2, 3), weight=1)
        self.grid_columnconfigure(0, weight=1)

        label = ctk.CTkLabel(master=self, text="No external memory storage found.", font=("Calibri", 40))
        label.grid(row=0, column=0, pady=20)

        img = None
        img = ctk.CTkImage(Image.open(additional_path + "/pendrive.png"), size=(300, 300))

        label = ctk.CTkLabel(master=self, image=img, text="")
        label.grid(row=1, column=0)

        button1 = ctk.CTkButton(self, text="Return to main menu", font=("Calibri", 30), width=300, height=50,
                                command=lambda: appController.set_frame(HomeFrame))
        button1.grid(row=2, column=0, padx=10, pady=10)
        button2 = ctk.CTkButton(self, text="Try again", font=("Calibri", 30), width=300, height=50,
                                command=lambda: appController.sign_document_choosen())
        button2.grid(row=3, column=0, padx=10, pady=10)


class FoundPendriveFrame(ctk.CTkFrame):
    """
    A class used to represent the Found Pendrive Frame of the application.


    Methods
    -------
    __init__(master: any, appController, name, pems):
        Initializes the Found Pendrive Frame with information about the found storage and .pem files.
    """

    def __init__(self, master: any, appController, name, pems):
        """
        Constructs all the necessary attributes for the FoundPendriveFrame object.

        Parameters
        ----------
            master : any
                The parent widget.
            appController : any
                The application controller.
            name : str
                The name of the found storage.
            pems : list
                The list of .pem files found in the storage.
        """
        super().__init__(master)

        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_rowconfigure((2, 3, 4), weight=2)
        self.grid_rowconfigure(3, weight=2)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)

        ctk.CTkLabel(master=self, text="Found storage:", font=("Calibri", 40)).grid(row=0, column=0, pady=30,
                                                                                    sticky="n", columnspan=2)
        ctk.CTkLabel(master=self, text=name, font=("Calibri", 40)).grid(row=1, column=0, pady=30, sticky="n",
                                                                        columnspan=2)

        if pems is None:
            ctk.CTkLabel(master=self, text="No .pem file found", font=("Calibri", 30)).grid(row=2, column=0, pady=30,
                                                                                            sticky="n", columnspan=2)
        else:
            ctk.CTkLabel(master=self, text="Select key:", font=("Calibri", 30)).grid(row=2, column=0, pady=20)
            combobox = ctk.CTkComboBox(master=self, values=pems, font=("Calibri", 30), width=500, height=50)
            combobox.grid(row=2, column=1, padx=10, pady=10)
            combobox.set(pems[0])

            button1 = ctk.CTkButton(self, text="Decode selected key", font=("Calibri", 30), width=300, height=50,
                                    command=lambda: appController.decrypt_key(combobox.get()))
            button1.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

        button2 = ctk.CTkButton(self, text="Return to main menu", font=("Calibri", 30), width=300, height=50,
                                command=lambda: appController.set_frame(HomeFrame))
        button2.grid(row=4, column=0, padx=10, pady=10, columnspan=2)


class PinEntryFrame(ctk.CTkFrame):
    """
    A class used to represent a Frame with a numerical keyboard and a text field for PIN entry.


    Methods
    -------
    __init__(master: any, appController, path, isPinWrong, isKeyForSignature, fileToDecryptPath):
        Initializes the Frame with a numerical keyboard and a text field for PIN entry.
    append_to_pin(number: str):
        Appends the given number to the PIN in the text field.
    """

    def __init__(self, master: any, appController, path, isPinWrong, isKeyForSignature, fileToDecryptPath):
        """
        Constructs all the necessary attributes for the PinEntryFrame object.

        Parameters
        ----------
            master : any
                The parent widget.
            appController : any
                The application controller.
            path : any
                Path to decrypted key.
            isPinWrong : bool
                Signalise if frame should display information about wrong pin.
            isKeyForSignature : bool
                Signalise if function is used for signature (True) or basic decrypting (False)
            fileToDecryptPath : str
                Path to file that is about to be decrypted. If isKeyForSignature == True, then fileToDecryptPath is None
        """
        super().__init__(master)
        self.appController = appController
        self.path = path
        self.pin = ""

        self.grid_rowconfigure((1, 2, 3, 4, 5), weight=1)
        self.grid_rowconfigure((0, 7), weight=2)
        self.grid_rowconfigure(6, weight=3)
        self.grid_columnconfigure((1, 2, 3), weight=1)
        self.grid_columnconfigure((0, 4), weight=2)

        self.pin_entry = ctk.CTkEntry(self, font=("Calibri", 30), width=300, height=50)
        self.pin_entry.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

        for i in range(9):
            button = ctk.CTkButton(self, text=str(i + 1), font=("Calibri", 30), width=100, height=50,
                                   command=lambda i=i: self.append_to_pin(str(i + 1)))
            button.grid(row=2 + i // 3, column=1 + i % 3, padx=10, pady=10)

        zero_button = ctk.CTkButton(self, text="0", font=("Calibri", 30), width=100, height=50,
                                    command=lambda: self.append_to_pin("0"))
        zero_button.grid(row=5, column=2, padx=10, pady=10)

        clear_button = ctk.CTkButton(self, text="C", font=("Calibri", 30), width=100, height=50,
                                     command=lambda: self.append_to_pin("-"))
        clear_button.grid(row=5, column=1, padx=10, pady=10)

        ok_button = ctk.CTkButton(self, text="OK", font=("Calibri", 30), width=100, height=50,
                                  command=lambda: self.ok_clicked(isKeyForSignature, fileToDecryptPath))
        ok_button.grid(row=5, column=3, padx=10, pady=10)

        if isPinWrong:
            label = ctk.CTkLabel(master=self, text="WRONG PIN", font=("Calibri", 20), text_color="red")
            label.grid(row=6, column=2)

        return_button = ctk.CTkButton(self, text="Return to main menu", font=("Calibri", 30), width=300, height=50,
                                      command=lambda: appController.set_frame(HomeFrame))
        return_button.grid(row=7, column=1, columnspan=3, padx=10, pady=10)

    def append_to_pin(self, number):
        """
        Appends the given number to the PIN in the text field or clears the field if "-" was passed as argument

        Parameters
        ----------
            number : str
                The number to append to the PIN.
        """
        if number == "-":
            self.pin_entry.delete(0, "end")
            self.pin = ""
        else:
            self.pin_entry.insert("end", "*")
            self.pin = self.pin + number

    def ok_clicked(self, isKeyForSignature, fileToDecryptPath):
        """
        Handles the click event of the OK button.
        """
        self.appController.handle_pin_entry(self.pin, self.path, isKeyForSignature, fileToDecryptPath)


class SelectFileToSignFrame(ctk.CTkFrame):
    """
    A class used to represent a Frame with a module to select file to sign.


    Methods
    -------
    __init__(master: any, appController, filePath, isExtensionValid):
        Initializes the Frame with a button to select a file to sign from the file's explorer.
    """

    def __init__(self, master: any, appController, filePath, isExtensionValid):
        """
        Constructs all the necessary attributes for the SelectFileToSignFrame object.

        Parameters
        ----------
            master : any
                The parent widget.
            appController : any
                The application controller.
            filePath : string or None
                Path to file if it has already been selected
            isExtensionValid : bool
                If the extension of selected file is valid. False if None file has been selected.
        """
        super().__init__(master)

        self.grid_rowconfigure((0, 1, 2, 4, 5, 6), weight=1)
        self.grid_columnconfigure(0, weight=1)

        select_file_button = ctk.CTkButton(self, text="Select file to sign", font=("Calibri", 30), width=300, height=50,
                                           command=lambda: appController.select_file_to_sign())
        select_file_button.grid(row=0, column=0, pady=30, sticky="n")

        if filePath is not None:
            filename_label = ctk.CTkLabel(master=self, text=filePath, font=("Calibri", 30))
            filename_label.grid(row=3, column=0, pady=30, sticky="n")
            if isExtensionValid:
                text_label = ctk.CTkLabel(master=self, text="Do you want to sign this file?", font=("Calibri", 30))
                text_label.grid(row=2, column=0, pady=30, sticky="n")
                sign_button = ctk.CTkButton(self, text="SIGN", font=("Calibri", 40), width=300,
                                            height=50, command=lambda: appController.sign_the_file(filePath))
                sign_button.grid(row=4, column=0, pady=30, sticky="n")
            else:
                text_label = ctk.CTkLabel(master=self, text="WRONG FILE EXTENSION", font=("Calibri", 30),
                                          text_color="red")
                text_label.grid(row=2, column=0, pady=30, sticky="n")

                img = None
                img = ctk.CTkImage(Image.open(additional_path + "/doc-fail.png"), size=(150, 150))

                label = ctk.CTkLabel(master=self, image=img, text="")
                label.grid(row=4, column=0)
        else:
            img = None
            img = ctk.CTkImage(Image.open(additional_path + "/file.png"), size=(300, 300))

            label = ctk.CTkLabel(master=self, image=img, text="")
            label.grid(row=2, rowspan=3, column=0)

        return_button = ctk.CTkButton(self, text="Return to main menu", font=("Calibri", 30), width=300, height=50,
                                      command=lambda: appController.set_frame(HomeFrame))
        return_button.grid(row=6, column=0, padx=10, pady=30)


class SelectFileToVerifyFrame(ctk.CTkFrame):
    """
        A class used to represent a Frame with a module to select file to verify.

        Methods
        -------
        __init__(master: any, appController, filePath, isExtensionValid):
            Initializes the Frame with a button to select a file to verify from the file's explorer.
        """

    def __init__(self, master: any, appController, filePath, isExtensionValid):
        """
        Constructs all the necessary attributes for the SelectFileToSignFrame object.

        Parameters
        ----------
            master : any
                The parent widget.
            appController : any
                The application controller.
            filePath : string or None
                Path to file if it has already been selected
            isExtensionValid : bool
                If the extension of selected file is valid. False if None file has been selected.
        """
        super().__init__(master)

        self.grid_rowconfigure((0, 1, 2, 4, 5, 6), weight=1)
        self.grid_columnconfigure(0, weight=1)

        select_file_button = ctk.CTkButton(self, text="Select file to verify", font=("Calibri", 30), width=300,
                                           height=50,
                                           command=lambda: appController.select_file_to_verify())
        select_file_button.grid(row=0, column=0, pady=30, sticky="n")

        if filePath is not None:
            filename_label = ctk.CTkLabel(master=self, text=filePath, font=("Calibri", 30), wraplength=700)
            filename_label.grid(row=3, column=0, pady=30, sticky="n")
            if isExtensionValid:
                text_label = ctk.CTkLabel(master=self, text="Do you want to verify this file?", font=("Calibri", 30))
                text_label.grid(row=2, column=0, pady=30, sticky="n")
                sign_button = ctk.CTkButton(self, text="Next", font=("Calibri", 40), width=300,
                                            height=50, command=lambda: appController.verify_signature(filePath))
                sign_button.grid(row=4, column=0, pady=30, sticky="n")
            else:
                text_label = ctk.CTkLabel(master=self, text="WRONG FILE EXTENSION", font=("Calibri", 30),
                                          text_color="red")
                text_label.grid(row=2, column=0, pady=30, sticky="n")

                img = None
                img = ctk.CTkImage(Image.open(additional_path + "/doc-fail.png"), size=(150, 150))

                label = ctk.CTkLabel(master=self, image=img, text="")
                label.grid(row=4, column=0)
        else:
            img = None
            img = ctk.CTkImage(Image.open(additional_path + "/file.png"), size=(300, 300))

            label = ctk.CTkLabel(master=self, image=img, text="")
            label.grid(row=2, rowspan=3, column=0)

        return_button = ctk.CTkButton(self, text="Return to main menu", font=("Calibri", 30), width=300, height=50,
                                      command=lambda: appController.set_frame(HomeFrame))
        return_button.grid(row=6, column=0, padx=10, pady=30)


class SelectPublicKeyFrame(ctk.CTkFrame):
    """
            A class used to represent a Frame with a module to select public key.


            Methods
            -------
            __init__(master: any, appController, filePath, isExtensionValid):
                Initializes the Frame with a button to select a file to verify from the file's explorer.
            """

    def __init__(self, master: any, appController, filePath, isExtensionValid, keyPath):
        """
        Constructs all the necessary attributes for the SelectFileToSignFrame object.

        Parameters
        ----------
            master : any
                The parent widget.
            appController : any
                The application controller.
            filePath : string or None
                Path to file
            isExtensionValid : bool
                If the extension of selected file is valid. False if None file has been selected.
        """
        super().__init__(master)

        self.grid_rowconfigure((0, 1, 2, 4, 5, 6), weight=1)
        self.grid_columnconfigure(0, weight=1)

        select_file_button = ctk.CTkButton(self, text="Select the public key", font=("Calibri", 30), width=300,
                                           height=50,
                                           command=lambda: appController.select_public_key(filePath))
        select_file_button.grid(row=0, column=0, pady=30, sticky="n")

        if keyPath is not None:
            filename_label = ctk.CTkLabel(master=self, text=keyPath, font=("Calibri", 30), wraplength=700)
            filename_label.grid(row=3, column=0, pady=30, sticky="n")
            if isExtensionValid:
                text_label = ctk.CTkLabel(master=self, text="Do you want to use this key?", font=("Calibri", 30))
                text_label.grid(row=2, column=0, pady=30, sticky="n")
                sign_button = ctk.CTkButton(self, text="Next", font=("Calibri", 40), width=300,
                                            height=50,
                                            command=lambda: appController.verify_signature2(filePath, keyPath))
                sign_button.grid(row=4, column=0, pady=30, sticky="n")
            else:
                text_label = ctk.CTkLabel(master=self, text="WRONG FILE EXTENSION", font=("Calibri", 30),
                                          text_color="red")
                text_label.grid(row=2, column=0, pady=30, sticky="n")

                img = None
                img = ctk.CTkImage(Image.open(additional_path + "/doc-fail.png"), size=(150, 150))

                label = ctk.CTkLabel(master=self, image=img, text="")
                label.grid(row=4, column=0)
        else:
            img = None
            img = ctk.CTkImage(Image.open(additional_path + "/key.png"), size=(300, 300))

            label = ctk.CTkLabel(master=self, image=img, text="")
            label.grid(row=2, rowspan=3, column=0)

        return_button = ctk.CTkButton(self, text="Return to main menu", font=("Calibri", 30), width=300, height=50,
                                      command=lambda: appController.set_frame(HomeFrame))
        return_button.grid(row=6, column=0, padx=10, pady=30)


class SelectXMLFrame(ctk.CTkFrame):
    """
            A class used to represent a Frame with a module to select public key.


            Methods
            -------
            __init__(master: any, appController, filePath, isExtensionValid):
                Initializes the Frame with a button to select a file to verify from the file's explorer.
            """

    def __init__(self, master: any, appController, filePath, keyPath, isExtensionValid, XMLPath):
        """
        Constructs all the necessary attributes for the SelectFileToSignFrame object.

        Parameters
        ----------
            master : any
                The parent widget.
            appController : any
                The application controller.
            filePath : string or None
                Path to file
            isExtensionValid : bool
                If the extension of selected file is valid. False if None file has been selected.
        """
        super().__init__(master)

        self.grid_rowconfigure((0, 1, 2, 4, 5, 6), weight=1)
        self.grid_columnconfigure(0, weight=1)

        select_file_button = ctk.CTkButton(self, text="Select the signature", font=("Calibri", 30), width=300,
                                           height=50,
                                           command=lambda: appController.select_signature(filePath, keyPath))
        select_file_button.grid(row=0, column=0, pady=30, sticky="n")

        if XMLPath is not None:
            filename_label = ctk.CTkLabel(master=self, text=XMLPath, font=("Calibri", 30), wraplength=700)
            filename_label.grid(row=3, column=0, pady=30, sticky="n")
            if isExtensionValid:
                text_label = ctk.CTkLabel(master=self, text="Do you want to use this signature?", font=("Calibri", 30))
                text_label.grid(row=2, column=0, pady=30, sticky="n")
                sign_button = ctk.CTkButton(self, text="Next", font=("Calibri", 40), width=300,
                                            height=50,
                                            command=lambda: appController.verify_signature3(filePath, keyPath, XMLPath))
                sign_button.grid(row=4, column=0, pady=30, sticky="n")
            else:
                text_label = ctk.CTkLabel(master=self, text="WRONG FILE EXTENSION", font=("Calibri", 30),
                                          text_color="red")
                text_label.grid(row=2, column=0, pady=30, sticky="n")

                img = None
                img = ctk.CTkImage(Image.open(additional_path + "/doc-fail.png"), size=(150, 150))

                label = ctk.CTkLabel(master=self, image=img, text="")
                label.grid(row=4, column=0)
        else:
            img = None
            img = ctk.CTkImage(Image.open(additional_path + "/certificate.png"), size=(300, 300))

            label = ctk.CTkLabel(master=self, image=img, text="")
            label.grid(row=2, rowspan=3, column=0)

        return_button = ctk.CTkButton(self, text="Return to main menu", font=("Calibri", 30), width=300, height=50,
                                      command=lambda: appController.set_frame(HomeFrame))
        return_button.grid(row=6, column=0, padx=10, pady=30)


class VerificationResultFrame(ctk.CTkFrame):
    """
    A class used to represent a Frame that displays the result of a verification operation.

    This Frame displays whether the verification was successful or not. It also provides an option to return to the main menu.


    Methods
    -------
    __init__(master: any, appController, result: bool):
        Initializes the VerificationResultFrame with the result of the verification operation.
    """

    def __init__(self, master: any, appController, result: bool):
        """
        Constructs all the necessary attributes for the VerificationResultFrame object.

        Parameters
        ----------
        master : any
            The parent widget.
        appController : any
            The application controller.
        result : bool
            The result of the verification operation. True if the verification was successful, False otherwise.
        """
        super().__init__(master)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=8)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        filename = ""
        if result:
            text_label = ctk.CTkLabel(self, text="VERIFICATION SUCCESSFUL", font=("Calibri", 40))
            filename = "success"
        else:
            text_label = ctk.CTkLabel(self, text="VERIFICATION FAILED", font=("Calibri", 40), text_color="red")
            filename = "failure"

        img = None
        img = ctk.CTkImage(Image.open(additional_path + "/" + filename + ".png"), size=(300, 300))

        label = ctk.CTkLabel(master=self, image=img, text="")
        label.grid(row=1, column=0)
        text_label.grid(row=0, column=0, pady=30, sticky="n")

        return_button = ctk.CTkButton(self, text="Return to main menu", font=("Calibri", 30), width=300, height=50,
                                      command=lambda: appController.set_frame(HomeFrame))
        return_button.grid(row=2, column=0, padx=10, pady=30)


class SelectEncryptDecryptFrame(ctk.CTkFrame):
    """
    A class used to represent a Frame with two options - encrypt od decrypt

    Methods
    -------
    __init__(master: any, appController, result: bool):
        Initializes the SelectEncryptDecryptFrame with option to either encrypt or decrypt a file.
    """

    def __init__(self, master: any, appController):
        """
        Constructs all the necessary attributes for the SelectEncryptDecryptFrame object.

        Parameters
        ----------
            master : any
                The parent widget.
            appController : any
                The application controller.
        """
        super().__init__(master)

        self.grid_rowconfigure((0, 1), weight=2)
        self.grid_rowconfigure(2, weight=4)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        img_locked = None
        img_locked = ctk.CTkImage(Image.open(additional_path + "/locked.png"), size=(250, 250))

        encrypt_button = ctk.CTkButton(self, image=img_locked, width=300, text="",
                                       height=300,
                                       command=lambda: appController.selected_encrypt())
        encrypt_button.grid(row=1, column=0, padx=10, pady=30)

        label_encrypt = ctk.CTkLabel(master=self, text="Encrypt", font=("Calibri", 40))
        label_encrypt.grid(row=2, column=0)

        img_unlocked = None
        img_unlocked = ctk.CTkImage(Image.open(additional_path + "/unlocked.png"), size=(250, 250))

        decrypt_button = ctk.CTkButton(self, image=img_unlocked, width=300, text="",
                                       height=300,
                                       command=lambda: appController.selected_decrypt())
        decrypt_button.grid(row=1, column=1, padx=10, pady=30)

        label_decrypt = ctk.CTkLabel(master=self, text="Decrypt", font=("Calibri", 40))
        label_decrypt.grid(row=2, column=1)

        return_button = ctk.CTkButton(self, text="Return to main menu", font=("Calibri", 30), width=300, height=50,
                                      command=lambda: appController.set_frame(HomeFrame))
        return_button.grid(row=3, column=0, columnspan=2, padx=10, pady=30)


class SelectFileToEncryptFrame(ctk.CTkFrame):
    """
    A class used to represent a Frame with option to chose file to encrypt

    Methods
    -------
    __init__(master: any, appController, filePath, isExtensionValid):
        Initializes the SelectFileToEncryptFrame with option to choose file to encrypt.
    """

    def __init__(self, master: any, appController, filePath, isExtensionValid):
        """
        Constructs all the necessary attributes for the SelectFileToEncryptFrame object.

        Parameters
        ----------
            master : any
                The parent widget.
            appController : any
                The application controller.
            filePath : string or None
                Path to file
            isExtensionValid : bool
                If the extension of selected file is valid. False if None file has been selected.
        """
        super().__init__(master)

        self.grid_rowconfigure((0, 1, 2, 4, 5, 6), weight=1)
        self.grid_columnconfigure(0, weight=1)

        select_file_button = ctk.CTkButton(self, text="Select file to encrypt", font=("Calibri", 30), width=300,
                                           height=50,
                                           command=lambda: appController.select_file_to_encrypt())
        select_file_button.grid(row=0, column=0, pady=30, sticky="n")

        if filePath is not None:
            filename_label = ctk.CTkLabel(master=self, text=filePath, font=("Calibri", 30), wraplength=700)
            filename_label.grid(row=3, column=0, pady=30, sticky="n")
            if isExtensionValid:
                text_label = ctk.CTkLabel(master=self, text="Do you want to encrypt this file?", font=("Calibri", 30))
                text_label.grid(row=2, column=0, pady=30, sticky="n")
                encrypt_button = ctk.CTkButton(self, text="Next", font=("Calibri", 40), width=300,
                                               height=50,
                                               command=lambda: appController.selected_file_to_encrypt(filePath))
                encrypt_button.grid(row=4, column=0, pady=30, sticky="n")
            else:
                text_label = ctk.CTkLabel(master=self, text="WRONG FILE EXTENSION", font=("Calibri", 30),
                                          text_color="red")
                text_label.grid(row=2, column=0, pady=30, sticky="n")

                img = None
                img = ctk.CTkImage(Image.open(additional_path + "/doc-fail.png"), size=(150, 150))

                label = ctk.CTkLabel(master=self, image=img, text="")
                label.grid(row=4, column=0)
        else:
            img = None
            img = ctk.CTkImage(Image.open(additional_path + "/locked.png"), size=(300, 300))

            label = ctk.CTkLabel(master=self, image=img, text="")
            label.grid(row=2, rowspan=3, column=0)

        return_button = ctk.CTkButton(self, text="Return to main menu", font=("Calibri", 30), width=300, height=50,
                                      command=lambda: appController.set_frame(HomeFrame))
        return_button.grid(row=6, column=0, padx=10, pady=30)


class SelectPublicKeyToEncryptFrame(ctk.CTkFrame):
    """
    A class used to represent a Frame with option to choose public key to encrypt

    Methods
    -------
    __init__(master: any, appController, filePath, keyPath, isExtensionValid):
        Initializes the SelectPublicKeyToEncryptFrame with option to choose public key to encrypt.
    """

    def __init__(self, master: any, appController, filePath, keyPath, isExtensionValid):
        """
        Constructs all the necessary attributes for the SelectPublicKeyToEncryptFrame object.

        Parameters
        ----------
            master : any
                The parent widget.
            appController : any
                The application controller.
            filePath : string
                Path to previously selected file
            keyPath : string or None
                Path to selected key
            isExtensionValid : bool
                If the extension of selected file is valid. False if None file has been selected.
        """
        super().__init__(master)

        self.grid_rowconfigure((0, 1, 2, 4, 5, 6), weight=1)
        self.grid_columnconfigure(0, weight=1)

        select_file_button = ctk.CTkButton(self, text="Select key to encrypt", font=("Calibri", 30), width=300,
                                           height=50,
                                           command=lambda: appController.select_public_key_to_encrypt(filePath))
        select_file_button.grid(row=0, column=0, pady=30, sticky="n")

        if keyPath is not None:
            keypath_label = ctk.CTkLabel(master=self, text=keyPath, font=("Calibri", 30), wraplength=700)
            keypath_label.grid(row=3, column=0, pady=30, sticky="n")
            if isExtensionValid:
                text_label = ctk.CTkLabel(master=self, text="Do you want to encrypt chosen file with this key?",
                                          font=("Calibri", 30))
                text_label.grid(row=2, column=0, pady=30, sticky="n")
                encrypt_button = ctk.CTkButton(self, text="Encrypt", font=("Calibri", 40), width=300,
                                               height=50,
                                               command=lambda: appController.encrypt_file(filePath, keyPath))
                encrypt_button.grid(row=4, column=0, pady=30, sticky="n")
            else:
                text_label = ctk.CTkLabel(master=self, text="WRONG FILE EXTENSION", font=("Calibri", 30),
                                          text_color="red")
                text_label.grid(row=2, column=0, pady=30, sticky="n")

                img = None
                img = ctk.CTkImage(Image.open(additional_path + "/doc-fail.png"), size=(150, 150))

                label = ctk.CTkLabel(master=self, image=img, text="")
                label.grid(row=4, column=0)
        else:
            img = None
            img = ctk.CTkImage(Image.open(additional_path + "/key.png"), size=(300, 300))

            label = ctk.CTkLabel(master=self, image=img, text="")
            label.grid(row=2, rowspan=3, column=0)

        return_button = ctk.CTkButton(self, text="Return to main menu", font=("Calibri", 30), width=300, height=50,
                                      command=lambda: appController.set_frame(HomeFrame))
        return_button.grid(row=6, column=0, padx=10, pady=30)


class SuccessfulOperationWithDisplay(ctk.CTkFrame):
    """
        A class used to represent a Frame with an information that some operation has been finished successfully.


        Methods ------- __init__(master: any, appController, infoHeader, valueDisplayed): Initializes the Frame with
        an information about successful operation and encrypted/decrypted string in a textbox.
    """

    def __init__(self, master: any, appController, infoHeader, valueDisplayed):
        """
        Constructs all the necessary attributes for the SuccessfulOperationWithDisplay object.

        Parameters
        ----------
            master : any
                The parent widget.
            appController : any
                The application controller.
            infoHeader : str
                Information displayed in header.
            valueDisplayed : str
                Information displayed in textbox.
        """
        super().__init__(master)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=8)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        text_label = ctk.CTkLabel(self, text=infoHeader, font=("Calibri", 30))
        text_label.grid(row=0, column=0, pady=30, sticky="n")

        textbox = ctk.CTkTextbox(self)
        textbox.grid(row=1, column=0, pady=0, padx=30, sticky='nsew')
        textbox.insert("0.0", valueDisplayed)
        textbox.configure(state='disabled')

        return_button = ctk.CTkButton(self, text="Return to main menu", font=("Calibri", 30), width=300, height=50,
                                      command=lambda: appController.set_frame(HomeFrame))
        return_button.grid(row=6, column=0, padx=10, pady=30)


class SelectFileToDecryptFrame(ctk.CTkFrame):
    """
    A class used to represent a Frame with option to chose file to decrypt

    Methods
    -------
    __init__(master: any, appController, filePath, isExtensionValid):
        Initializes the SelectFileToDecryptFrame with option to choose file to decrypt.
    """

    def __init__(self, master: any, appController, filePath, isExtensionValid):
        """
        Constructs all the necessary attributes for the SelectFileToDecryptFrame object.

        Parameters
        ----------
            master : any
                The parent widget.
            appController : any
                The application controller.
            filePath : string or None
                Path to file
            isExtensionValid : bool
                If the extension of selected file is valid. False if None file has been selected.
        """
        super().__init__(master)

        self.grid_rowconfigure((0, 1, 2, 4, 5, 6), weight=1)
        self.grid_columnconfigure(0, weight=1)

        select_file_button = ctk.CTkButton(self, text="Select file to decrypt", font=("Calibri", 30), width=300,
                                           height=50,
                                           command=lambda: appController.select_file_to_decrypt())
        select_file_button.grid(row=0, column=0, pady=30, sticky="n")

        if filePath is not None:
            filename_label = ctk.CTkLabel(master=self, text=filePath, font=("Calibri", 30), wraplength=700)
            filename_label.grid(row=3, column=0, pady=30, sticky="n")
            if isExtensionValid:
                text_label = ctk.CTkLabel(master=self, text="Do you want to decrypt this file?", font=("Calibri", 30))
                text_label.grid(row=2, column=0, pady=30, sticky="n")
                encrypt_button = ctk.CTkButton(self, text="Next", font=("Calibri", 40), width=300,
                                               height=50,
                                               command=lambda: appController.selected_file_to_decrypt(filePath))
                encrypt_button.grid(row=4, column=0, pady=30, sticky="n")
            else:
                text_label = ctk.CTkLabel(master=self, text="WRONG FILE EXTENSION", font=("Calibri", 30),
                                          text_color="red")
                text_label.grid(row=2, column=0, pady=30, sticky="n")

                img = None
                img = ctk.CTkImage(Image.open(additional_path + "/doc-fail.png"), size=(150, 150))

                label = ctk.CTkLabel(master=self, image=img, text="")
                label.grid(row=4, column=0)
        else:
            img = None
            img = ctk.CTkImage(Image.open(additional_path + "/unlocked.png"), size=(300, 300))

            label = ctk.CTkLabel(master=self, image=img, text="")
            label.grid(row=2, rowspan=3, column=0)

        return_button = ctk.CTkButton(self, text="Return to main menu", font=("Calibri", 30), width=300, height=50,
                                      command=lambda: appController.set_frame(HomeFrame))
        return_button.grid(row=6, column=0, padx=10, pady=30)


class NoPendriveForDecryptionFrame(ctk.CTkFrame):
    """
    A class used to represent the NoPendriveForDecryptionFrame of the application.


    Methods
    -------
    __init__(master: any, appController, filePath):
        Initializes the NoPendriveForDecryptionFrame with a message and buttons for retry or return to main menu.
    """

    def __init__(self, master: any, appController, filePath):
        """
        Constructs all the necessary attributes for the NoPendriveFrame object.

        Parameters
        ----------
            master : any
                The parent widget.
            appController : any
                The application controller.
            filePath : str
                Path to file which is about to be decrypted.
        """
        super().__init__(master)

        self.grid_rowconfigure(1, weight=9)
        self.grid_rowconfigure((0, 2, 3), weight=1)
        self.grid_columnconfigure(0, weight=1)

        label = ctk.CTkLabel(master=self, text="No external memory storage found.", font=("Calibri", 40))
        label.grid(row=0, column=0, pady=20)

        img = None
        img = ctk.CTkImage(Image.open(additional_path + "/pendrive.png"), size=(300, 300))

        label = ctk.CTkLabel(master=self, image=img, text="")
        label.grid(row=1, column=0)

        button1 = ctk.CTkButton(self, text="Return to main menu", font=("Calibri", 30), width=300, height=50,
                                command=lambda: appController.set_frame(HomeFrame))
        button1.grid(row=2, column=0, padx=10, pady=10)
        button2 = ctk.CTkButton(self, text="Try again", font=("Calibri", 30), width=300, height=50,
                                command=lambda: appController.selected_file_to_decrypt(filePath))
        button2.grid(row=3, column=0, padx=10, pady=10)


class FoundPendriveForDecryptionFrame(ctk.CTkFrame):
    """
    A class used to represent the FoundPendriveForDecryptionFrame of the application.


    Methods
    -------
    __init__(master: any, appController, name, pems, filePath):
        Initializes the FoundPendriveForDecryptionFrame with information about the found storage and .pem files.
    """

    def __init__(self, master: any, appController, name, pems, filePath):
        """
        Constructs all the necessary attributes for the FoundPendriveForDecryptionFrame object.

        Parameters
        ----------
            master : any
                The parent widget.
            appController : any
                The application controller.
            name : str
                The name of the found storage.
            pems : list
                The list of .pem files found in the storage.
            filePath : str
                Path to file that is about to be decrypted.
        """
        super().__init__(master)

        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_rowconfigure((2, 3, 4), weight=2)
        self.grid_rowconfigure(3, weight=2)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)

        ctk.CTkLabel(master=self, text="Found storage:", font=("Calibri", 40)).grid(row=0, column=0, pady=30,
                                                                                    sticky="n", columnspan=2)
        ctk.CTkLabel(master=self, text=name, font=("Calibri", 40)).grid(row=1, column=0, pady=30, sticky="n",
                                                                        columnspan=2)

        if pems is None:
            ctk.CTkLabel(master=self, text="No .pem file found", font=("Calibri", 30)).grid(row=2, column=0, pady=30,
                                                                                            sticky="n", columnspan=2)
        else:
            ctk.CTkLabel(master=self, text="Select key:", font=("Calibri", 30)).grid(row=2, column=0, pady=20)
            combobox = ctk.CTkComboBox(master=self, values=pems, font=("Calibri", 30), width=500, height=50)
            combobox.grid(row=2, column=1, padx=10, pady=10)
            combobox.set(pems[0])

            button1 = ctk.CTkButton(self, text="Decode selected key", font=("Calibri", 30), width=300, height=50,
                                    command=lambda: appController.selected_decrypt_key_for_file_decryption
                                    (combobox.get(), filePath))
            button1.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

        button2 = ctk.CTkButton(self, text="Return to main menu", font=("Calibri", 30), width=300, height=50,
                                command=lambda: appController.set_frame(HomeFrame))
        button2.grid(row=4, column=0, padx=10, pady=10, columnspan=2)
