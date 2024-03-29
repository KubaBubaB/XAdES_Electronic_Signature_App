import os.path

import customtkinter as ctk
from PIL import Image, ImageTk


class HomeFrame(ctk.CTkFrame):
    """
    A class used to represent the Home Frame of the application.

    ...

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

        label = ctk.CTkLabel(master=self, text="SIGNATURE ENCRYPTION APP", font=("Georgia", 50))
        label.grid(row=0, column=0, columnspan=2)

        sign_button = ctk.CTkButton(self, text="Sign the document", font=("Calibri", 40), width=400, height=60,
                                    command=lambda: appController.sign_document_choosen())
        sign_button.grid(row=1, column=0, padx=10, pady=1)

        validate_button = ctk.CTkButton(self, text="Verify signature", font=("Calibri", 40), width=400, height=60,
                                        command=lambda: appController.set_frame(SelectFileToVerifyFrame, None, None))
        validate_button.grid(row=2, column=0, padx=10, pady=1)

        encrypt_button = ctk.CTkButton(self, text="Encryption/decryption", font=("Calibri", 40), width=400, height=60)
        encrypt_button.grid(row=3, column=0, padx=10, pady=1)

        about_button = ctk.CTkButton(self, text="About app", font=("Calibri", 40), width=400, height=60)
        about_button.grid(row=4, column=0, padx=10, pady=1)

        img = None
        if os.path.exists("icons/certificate.png"):
            img = ctk.CTkImage(Image.open("icons/certificate.png"), size=(300, 300))
        elif os.path.exists("SignatureEncryptionApp/icons/certificate.png"):
            img = ctk.CTkImage(Image.open("icons/certificate.png"), size=(300, 300))
        label = ctk.CTkLabel(master=self, image=img, text="")
        label.grid(row=1, column=1, rowspan=4)


class NoPendriveFrame(ctk.CTkFrame):
    """
    A class used to represent the No Pendrive Frame of the application.

    ...

    Methods
    -------
    __init__(master: any, appController):
        Initializes the No Pendrive Frame with a message and buttons for retry or return to main menu.
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
        if os.path.exists("icons/pendrive.png"):
            img = ctk.CTkImage(Image.open("icons/pendrive.png"), size=(300, 300))
        elif os.path.exists("SignatureEncryptionApp/icons/pendrive.png"):
            img = ctk.CTkImage(Image.open("icons/pendrive.png"), size=(300, 300))

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

    ...

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

    ...

    Methods
    -------
    __init__(master: any, appController, path, isPinWrong):
        Initializes the Frame with a numerical keyboard and a text field for PIN entry.
    append_to_pin(number: str):
        Appends the given number to the PIN in the text field.
    """

    def __init__(self, master: any, appController, path, isPinWrong):
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
                                  command=self.ok_clicked)
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

    def ok_clicked(self):
        """
        Handles the click event of the OK button.
        """
        self.appController.handle_pin_entry(self.pin, self.path)


class SelectFileToSignFrame(ctk.CTkFrame):
    """
    A class used to represent a Frame with a module to select file to sign.

    ...

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
                if os.path.exists("icons/doc-fail.png"):
                    img = ctk.CTkImage(Image.open("icons/doc-fail.png"), size=(150, 150))
                elif os.path.exists("SignatureEncryptionApp/icons/doc-fail.png"):
                    img = ctk.CTkImage(Image.open("icons/doc-fail.png"), size=(150, 150))

                label = ctk.CTkLabel(master=self, image=img, text="")
                label.grid(row=4, column=0)
        else:
            img = None
            if os.path.exists("icons/file.png"):
                img = ctk.CTkImage(Image.open("icons/file.png"), size=(300, 300))
            elif os.path.exists("SignatureEncryptionApp/icons/file.png"):
                img = ctk.CTkImage(Image.open("icons/file.png"), size=(300, 300))

            label = ctk.CTkLabel(master=self, image=img, text="")
            label.grid(row=2, rowspan=3, column=0)

        return_button = ctk.CTkButton(self, text="Return to main menu", font=("Calibri", 30), width=300, height=50,
                                      command=lambda: appController.set_frame(HomeFrame))
        return_button.grid(row=6, column=0, padx=10, pady=30)


class FileSignedFrame(ctk.CTkFrame):
    """
    A class used to represent a Frame with an information that file has been signed successfully.

    ...

    Methods
    -------
    __init__(master: any, appController, filePath, isExtensionValid):
        Initializes the Frame with an information about successful signing and XML signature in textbox.
    """

    def __init__(self, master: any, appController, signature):
        """
        Constructs all the necessary attributes for the SelectFileToSignFrame object.

        Parameters
        ----------
            master : any
                The parent widget.
            appController : any
                The application controller.
            signature : str
                The XAdES representation of signature
        """
        super().__init__(master)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=8)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        text_label = ctk.CTkLabel(self, text="SIGNATURE CREATED", font=("Calibri", 30))
        text_label.grid(row=0, column=0, pady=30, sticky="n")

        textbox = ctk.CTkTextbox(self)
        textbox.grid(row=1, column=0, pady=0, padx=30, sticky='nsew')
        textbox.insert("0.0", signature)
        textbox.configure(state='disabled')


        return_button = ctk.CTkButton(self, text="Return to main menu", font=("Calibri", 30), width=300, height=50,
                                      command=lambda: appController.set_frame(HomeFrame))
        return_button.grid(row=6, column=0, padx=10, pady=30)


class SelectFileToVerifyFrame(ctk.CTkFrame):
    """
        A class used to represent a Frame with a module to select file to verify.

        ...

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
                if os.path.exists("icons/doc-fail.png"):
                    img = ctk.CTkImage(Image.open("icons/doc-fail.png"), size=(150, 150))
                elif os.path.exists("SignatureEncryptionApp/icons/doc-fail.png"):
                    img = ctk.CTkImage(Image.open("icons/doc-fail.png"), size=(150, 150))

                label = ctk.CTkLabel(master=self, image=img, text="")
                label.grid(row=4, column=0)
        else:
            img = None
            if os.path.exists("icons/file.png"):
                img = ctk.CTkImage(Image.open("icons/file.png"), size=(300, 300))
            elif os.path.exists("SignatureEncryptionApp/icons/file.png"):
                img = ctk.CTkImage(Image.open("icons/file.png"), size=(300, 300))

            label = ctk.CTkLabel(master=self, image=img, text="")
            label.grid(row=2, rowspan=3, column=0)

        return_button = ctk.CTkButton(self, text="Return to main menu", font=("Calibri", 30), width=300, height=50,
                                      command=lambda: appController.set_frame(HomeFrame))
        return_button.grid(row=6, column=0, padx=10, pady=30)


class SelectPublicKeyFrame(ctk.CTkFrame):
    """
            A class used to represent a Frame with a module to select public key.

            ...

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
                if os.path.exists("icons/doc-fail.png"):
                    img = ctk.CTkImage(Image.open("icons/doc-fail.png"), size=(150, 150))
                elif os.path.exists("SignatureEncryptionApp/icons/doc-fail.png"):
                    img = ctk.CTkImage(Image.open("icons/doc-fail.png"), size=(150, 150))

                label = ctk.CTkLabel(master=self, image=img, text="")
                label.grid(row=4, column=0)
        else:
            img = None
            if os.path.exists("icons/key.png"):
                img = ctk.CTkImage(Image.open("icons/key.png"), size=(300, 300))
            elif os.path.exists("SignatureEncryptionApp/icons/key.png"):
                img = ctk.CTkImage(Image.open("icons/key.png"), size=(300, 300))

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
                if os.path.exists("icons/doc-fail.png"):
                    img = ctk.CTkImage(Image.open("icons/doc-fail.png"), size=(150, 150))
                elif os.path.exists("SignatureEncryptionApp/icons/doc-fail.png"):
                    img = ctk.CTkImage(Image.open("icons/doc-fail.png"), size=(150, 150))

                label = ctk.CTkLabel(master=self, image=img, text="")
                label.grid(row=4, column=0)
        else:
            img = None
            if os.path.exists("icons/certificate.png"):
                img = ctk.CTkImage(Image.open("icons/certificate.png"), size=(300, 300))
            elif os.path.exists("SignatureEncryptionApp/icons/certificate.png"):
                img = ctk.CTkImage(Image.open("icons/certificate.png"), size=(300, 300))

            label = ctk.CTkLabel(master=self, image=img, text="")
            label.grid(row=2, rowspan=3, column=0)

        return_button = ctk.CTkButton(self, text="Return to main menu", font=("Calibri", 30), width=300, height=50,
                                      command=lambda: appController.set_frame(HomeFrame))
        return_button.grid(row=6, column=0, padx=10, pady=30)


class VerificationResultFrame(ctk.CTkFrame):
    """
    A class used to represent a Frame with an information about verification result.
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
                The result of verification.
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
        if os.path.exists("icons/" + filename + ".png"):
            img = ctk.CTkImage(Image.open("icons/" + filename + ".png"), size=(300, 300))
        elif os.path.exists("SignatureEncryptionApp/icons/" + filename + ".png"):
            img = ctk.CTkImage(Image.open("icons/" + filename + ".png"), size=(300, 300))

        label = ctk.CTkLabel(master=self, image=img, text="")
        label.grid(row=1, column=0)
        text_label.grid(row=0, column=0, pady=30, sticky="n")

        return_button = ctk.CTkButton(self, text="Return to main menu", font=("Calibri", 30), width=300, height=50,
                                      command=lambda: appController.set_frame(HomeFrame))
        return_button.grid(row=2, column=0, padx=10, pady=30)
