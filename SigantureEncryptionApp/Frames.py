import customtkinter as ctk
import time

class HomeFrame(ctk.CTkFrame):
    def __init__(self, master: any, appController):
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
    def __init__(self, master: any, appController):
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
    def __init__(self, master: any, appController, name, pems):
        super().__init__(master)

        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.grid_rowconfigure(3, weight=2)
        self.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(master=self, text="Found storage:", font=("Calibri", 30)).grid(row=0, column=0, pady=30, sticky="n")
        ctk.CTkLabel(master=self, text=name, font=("Calibri", 30)).grid(row=1, column=0, pady=30, sticky="n")

        if pems is None:
            ctk.CTkLabel(master=self, text="No .pem file found", font=("Calibri", 30)).grid(row=2, column=0, pady=30, sticky="n")
        else:
            combobox = ctk.CTkComboBox(master=self, values=pems, font=("Calibri", 30), width=300, height=50)
            combobox.grid(row=2, column=0, padx=10, pady=10)
            combobox.set(pems[0])

            button1 = ctk.CTkButton(self, text="Decode selected key", font=("Calibri", 30), width=300, height=50,
                                    command=lambda: appController.encrypt_key(combobox.get()))
            button1.grid(row=3, column=0, padx=10, pady=10)

        button2 = ctk.CTkButton(self, text="Return to main menu", font=("Calibri", 30), width=300, height=50,
                                command=lambda: appController.set_frame(HomeFrame))
        button2.grid(row=4, column=0, padx=10, pady=10)