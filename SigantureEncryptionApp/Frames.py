import customtkinter as ctk
import time


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

        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure(0, weight=1)

        button1 = ctk.CTkButton(self, text="Sign the document", font=("Calibri", 40), width=500, height=120,
                                command=lambda: appController.sign_document_choosen())
        button1.grid(row=0, column=0, padx=10, pady=10)

        button2 = ctk.CTkButton(self, text="Validate signing", font=("Calibri", 40), width=500, height=120)
        button2.grid(row=1, column=0, padx=10, pady=10)

        button3 = ctk.CTkButton(self, text="Basic encryption/decryption", font=("Calibri", 40), width=500, height=120)
        button3.grid(row=2, column=0, padx=10, pady=10)


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

        self.grid_rowconfigure(0, weight=9)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        label = ctk.CTkLabel(master=self, text="No external memory storage found.", font=("Calibri", 30))
        label.grid(row=0, column=0, pady=30, sticky="n")

        button1 = ctk.CTkButton(self, text="Return to main menu", font=("Calibri", 30), width=300, height=50,
                                command=lambda: appController.set_frame(HomeFrame))
        button1.grid(row=1, column=0, padx=10, pady=10)
        button2 = ctk.CTkButton(self, text="Try again", font=("Calibri", 30), width=300, height=50,
                                command=lambda: appController.sign_document_choosen())
        button2.grid(row=2, column=0, padx=10, pady=10)


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

        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.grid_rowconfigure(3, weight=2)
        self.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(master=self, text="Found storage:", font=("Calibri", 30)).grid(row=0, column=0, pady=30,
                                                                                    sticky="n")
        ctk.CTkLabel(master=self, text=name, font=("Calibri", 30)).grid(row=1, column=0, pady=30, sticky="n")

        if pems is None:
            ctk.CTkLabel(master=self, text="No .pem file found", font=("Calibri", 30)).grid(row=2, column=0, pady=30,
                                                                                            sticky="n")
        else:
            combobox = ctk.CTkComboBox(master=self, values=pems, font=("Calibri", 30), width=300, height=50)
            combobox.grid(row=2, column=0, padx=10, pady=10)
            combobox.set(pems[0])

            button1 = ctk.CTkButton(self, text="Decode selected key", font=("Calibri", 30), width=300, height=50,
                                    command=lambda: appController.decrypt_key(combobox.get()))
            button1.grid(row=3, column=0, padx=10, pady=10)

        button2 = ctk.CTkButton(self, text="Return to main menu", font=("Calibri", 30), width=300, height=50,
                                command=lambda: appController.set_frame(HomeFrame))
        button2.grid(row=4, column=0, padx=10, pady=10)


class PinEntryFrame(ctk.CTkFrame):
    """
    A class used to represent a Frame with a numerical keyboard and a text field for PIN entry.

    ...

    Methods
    -------
    __init__(master: any, appController):
        Initializes the Frame with a numerical keyboard and a text field for PIN entry.
    append_to_pin(number: str):
        Appends the given number to the PIN in the text field.
    """

    def __init__(self, master: any, appController, path):
        """
        Constructs all the necessary attributes for the PinEntryFrame object.

        Parameters
        ----------
            master : any
                The parent widget.
            appController : any
                The application controller.
        """
        super().__init__(master)
        self.appController = appController
        self.path = path

        self.pin_entry = ctk.CTkEntry(self, font=("Calibri", 30), width=300, height=50)
        self.pin_entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        for i in range(9):
            button = ctk.CTkButton(self, text=str(i + 1), font=("Calibri", 30), width=100, height=50,
                                   command=lambda i=i: self.append_to_pin(str(i + 1)))
            button.grid(row=1 + i // 3, column=i % 3, padx=10, pady=10)

        zero_button = ctk.CTkButton(self, text="0", font=("Calibri", 30), width=100, height=50,
                                    command=lambda: self.append_to_pin("0"))
        zero_button.grid(row=4, column=0, padx=10, pady=10)

        ok_button = ctk.CTkButton(self, text="OK", font=("Calibri", 30), width=100, height=50,
                                  command=self.ok_clicked)
        ok_button.grid(row=4, column=2, padx=10, pady=10)

    def append_to_pin(self, number):
        """
        Appends the given number to the PIN in the text field.

        Parameters
        ----------
            number : str
                The number to append to the PIN.
        """
        self.pin_entry.insert("end", number)

    def ok_clicked(self):
        """
        Handles the click event of the OK button.
        """
        pin = self.pin_entry.get()
        self.appController.handle_pin_entry(pin, self.path)
