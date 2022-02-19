"""
Author: Rob Dunsmuir
Date: Feburary 19, 2022
Purpose: UI file, set up the interface, menu, manages the texteditor
"""

import tkinter
from tkinter import *


class MyUi:

    def __init__(self, config):
        self.root = tkinter.Tk()
        self.file = None

        # text editor
        self.textEditor = Text(self.root, width=config.EDITOR_WIDTH, height=config.EDITOR_HEIGHT)
        self.textEditor.pack()

        self.root.geometry(config.WINDOW_SIZE)
        self.root.title(config.TITLE)

        # menu
        menu_bar = tkinter.Menu(self.root)
        menu_bar.add_command(label="New", command=lambda: self.file.new_file())
        menu_bar.add_command(label="Open", command=lambda: self.file.open_file())
        menu_bar.add_command(label="Save", command=lambda: self.file.save_file())

        self.root.config(menu=menu_bar)

    def clear_editor(self):
        self.textEditor.delete('1.0', END)

    def set_title(self, title):
        self.root.title(title)

    def set_file(self, file):
        self.file = file
