"""
Author: Rob Dunsmuir
Date: Feburary 19, 2022
Purpose: Config class, stores variables for use in the application 
"""

import os

class Config:

    def __init__(self):
        self.FILENAME = ""
        self.ORIG_CONTENT = ""
        self.EDITOR_WIDTH = 58
        self.EDITOR_HEIGHT= 17
        self.WINDOW_SIZE = "500x300"
        self.TITLE = "Python Notes App"
        self.FILENAME_LENGTH = 10
        self.FILE_EXT = ".txt"
        self.FILE_PATH = os.getcwd()
        self.FILE_FOLDER = self.FILE_PATH+"\\files\\"
        print(self.FILE_FOLDER)
