import os
import time

import customtkinter as ctk
import Frames as fr
import Scripts

class AppController(ctk.CTk):
    width_ = 800
    height_ = 600
    current_ = None
    frames_ = {}
    text_ = ""

    def __init__(self):
        super().__init__()

        self.title("Singature Encryption App")
        self.geometry(f"{self.width_}x{self.height_}")
        self.resizable(False, False)
        ctk.set_appearance_mode("Dark")

        self.set_frame(fr.HomeFrame)

    def sign_document_choosen(self):
        storage = Scripts.check_external_storage()
        if storage is not None:
            pems = Scripts.find_pem_files(storage)
            self.set_frame(fr.FoundPendriveFrame, storage, pems)
        else:
            self.set_frame(fr.NoPendriveFrame)

    def set_frame(self, frame_name, *args):
        if self.current_ is not None:
            self.current_.pack_forget()
        self.current_ = frame_name(self, self, *args)
        self.current_.pack(expand=True, fill="both")

    def encrypt_key(self, name):
        print(name)