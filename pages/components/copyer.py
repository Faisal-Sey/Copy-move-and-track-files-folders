import os
from tkinter import *
from . import trackers, callbacks
from copy import deepcopy
from tkinter.ttk import Progressbar
import shutil

#   start of copying function
#       start of copying files function

total_files = 0
total_size = None
progress_label = None
progress = None
percentage = None
app = None
file_sizes = []
files_total = 0
copy_file_sizes = None
FILE_SIZE = 0

def copy_files(**kwargs):
    global total_files, files_total, file_sizes, copy_file_sizes, FILE_SIZE, progress_label, progress, percentage, app, total_size 
    src_text_widget = kwargs["src_text_widget"]
    dest_text_widget = kwargs["dest_text_widget"]
    file_source_is_not_empty = kwargs["file_source_is_not_empty"]
    destination_is_not_empty = kwargs["destination_is_not_empty"]
    canvas = kwargs["canvas"]
    app = kwargs["app"]
    destination = kwargs["destination"]
    progress_image = kwargs["progress_image"]
    sources = kwargs["sources"]

    src_text_widget.delete("0.0", "insert")
    dest_text_widget.delete("0.0", "insert")
    if file_source_is_not_empty and destination_is_not_empty:
        try:
            trackers.track_contents.place_forget()
            trackers.success_content_scrolled_text.place_forget()
            trackers.unsuccess_content_scrolled_text.place_forget()
            trackers.table_header.place_forget()
        except NameError:
            pass
        list_contents = Frame(canvas, width=1030, height=290, bg="#ebe9e9")
        progress_label = Label(list_contents, image=progress_image)
        progress_label.place(anchor="c", relx=0.5, rely=0.2)
        progress = Progressbar(list_contents, orient=HORIZONTAL, length=100,
                               mode='determinate')

        progress.place(anchor="c", relx=0.5, rely=0.45, width=150, height=30)
        files_total = Label(list_contents, text="Total Files: 0/0", bg="#ebe9e9")
        files_total.place(anchor="c", relx=0.5, rely=0.65)
        total_size = Label(list_contents, text="Total Size: 0/0", bg="#ebe9e9")
        total_size.place(anchor="c", relx=0.5, rely=0.74)
        percentage = Label(list_contents, text="Percentage: 0/100", bg="#ebe9e9")
        percentage.place(anchor="c", relx=0.5, rely=0.83)
        list_contents.place(anchor="c", relx=0.39, rely=0.8)
        progress_title = Label(app, text="Progress Bar", bg="white")
        progress_title.place(anchor="c", relx=0.10, rely=0.598)

        total_files = 0
        i = 1
        for file in sources:
            total_files = total_files + 1
            file_sizes.append(int(os.path.getsize(file)))
        copy_file_sizes = deepcopy(file_sizes)
        FILE_SIZE = sum(file_sizes)
        try:
            for file in sources:
                shutil.copy(file, destination, callbacks.callback_function)
        except shutil.SameFileError:
            pass


#       end of files copying function
#       start of folders copying function


def copy_folders(**kwargs):
    global total_files, files_total, file_sizes, copy_file_sizes, FILE_SIZE
    src_text_widget = kwargs["src_text_widget"]
    dest_text_widget = kwargs["dest_text_widget"]
    folder_source_is_not_empty = kwargs["folder_source_is_not_empty"]
    destination_is_not_empty = kwargs["destination_is_not_empty"]
    canvas = kwargs["canvas"]
    app = kwargs["app"]
    destination = kwargs["destination"]
    progress_image = kwargs["progress_image"]
    sources = kwargs["sources"]

    src_text_widget.delete("0.0", "insert")
    dest_text_widget.delete("0.0", "insert")
    
    if folder_source_is_not_empty and destination_is_not_empty:
        try:
            trackers.track_contents.place_forget()
            trackers.success_content_scrolled_text.place_forget()
            trackers.unsuccess_content_scrolled_text.place_forget()
            trackers.table_header.place_forget()
        except NameError:
            pass
        except AttributeError:
            pass
        list_contents = Frame(canvas, width=1030, height=290, bg="#ebe9e9")
        progress_label = Label(list_contents, image=progress_image)
        progress_label.place(anchor="c", relx=0.5, rely=0.2)
        progress = Progressbar(list_contents, orient=HORIZONTAL, length=100,
                               mode='determinate')

        progress.place(anchor="c", relx=0.5, rely=0.45, width=150, height=30)
        files_total = Label(list_contents, text="Total Files: 0/0", bg="#ebe9e9")
        files_total.place(anchor="c", relx=0.5, rely=0.65)
        total_size = Label(list_contents, text="Total Size: 0/0", bg="#ebe9e9")
        total_size.place(anchor="c", relx=0.5, rely=0.74)
        percentage = Label(list_contents, text="Percentage: 0/100", bg="#ebe9e9")
        percentage.place(anchor="c", relx=0.5, rely=0.83)
        list_contents.place(anchor="c", relx=0.39, rely=0.8)
        progress_title = Label(app, text="Progress Bar", bg="white")
        progress_title.place(anchor="c", relx=0.10, rely=0.598)

        file_list = os.scandir(sources)
        file_sizes = []
        total_files = 0
        for file in file_list:
            if file.is_dir():
                folder = os.listdir(file.path)
                for inner_file in folder:
                    inner_file = '/'.join(file.path.split('\\')) + '/' + inner_file
                    file_sizes.append(int(os.path.getsize(inner_file)))
                    total_files = total_files + 1

            elif file.is_file():
                file_sizes.append(int(os.path.getsize(file.path)))
                total_files = total_files + 1
        copy_file_sizes = deepcopy(file_sizes)
        FILE_SIZE = sum(file_sizes)
        try:
            shutil.copytree(sources, destination + "/" + sources.split("/")[-1], callbacks.callback_function_folder)
        except FileExistsError:
            pass
        # for x in range(1, total_files + 1):
        #     time.sleep(1)
        #     bars_folder(x)


#       end of folder copying function
#   end of copying function

#   inserting into Texts
#       add text to folder source entry
