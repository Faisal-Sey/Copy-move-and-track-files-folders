import os
from . import copyer

#   start move files n folders function
#       move files function


def move_files(sources):
    copyer.copy_files()
    for file in sources:
        os.remove(file)


# move folder function


def move_folder(sources):
    copyer.copy_folders()
    os.remove(sources)

