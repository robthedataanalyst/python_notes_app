"""
Author: Rob Dunsmuir
Date: Feburary 19, 2022
Purpose: Main file, sets up objects
"""

import config
import file
import ui

if __name__ == "__main__":

    myConfig = config.Config()
    myUi = ui.MyUi(myConfig)
    myFile = file.File(myUi, myConfig)
    myUi.set_file(myFile)

    myUi.root.mainloop()
