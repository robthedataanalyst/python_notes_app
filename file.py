"""
Author: Rob Dunsmuir
Date: Feburary 19, 2022
Purpose: File class, reading/writing files, generating random filenames
"""

import random
import string
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox
import encrypt

class File:

    def __init__(self, ui, config):
        self.ui = ui
        self.config = config

    def new_file(self):
        self.ui.clear_editor()
        self.config.FILENAME = ""
        self.config.ORIG_CONTENT = ""

    def open_file(self):
        self.config.ORIG_CONTENT = ""
        tmp_filename = fd.askopenfilename()
        self.config.FILENAME = tmp_filename.split("/",)[-1]
        with open(tmp_filename) as f:
            data = f.readlines()
        f.close()

        # TODO: add message box prompt for salt value for encryption/decryption

        for line in data:
            self.config.ORIG_CONTENT += line
        self.ui.textEditor.insert('1.0', self.config.ORIG_CONTENT)
        self.ui.root.title("Editing: "+self.config.FILENAME)

    def save_file(self):
        mode = "r+"
        if self.config.FILENAME == "":
            self.config.FILENAME = self.generate_filename()+self.config.FILE_EXT
            mode = 'w'

        text = self.ui.textEditor.get(0.1, tk.END)

        # encrypt here

        with open(self.config.FILE_FOLDER+self.config.FILENAME, mode) as f:
            f.write(text)
        f.close()
        self.show_message("File Saved")

    def show_message(self, message):
        messagebox.showinfo(title="Action", message=message)

    def generate_filename(self):
        return "".join(random.choice(string.ascii_letters + string.digits) for i in range(self.config.FILENAME_LENGTH))
