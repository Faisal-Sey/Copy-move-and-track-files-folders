import os, tkinter
from tkinter import *
from tkinter.scrolledtext import ScrolledText

#   start of file and folder trackers
#       start of files tracker

track_contents = None
success_content_scrolled_text = None
unsuccess_content_scrolled_text = None
table_header = None

def track_files(**kwargs):
    destination = kwargs["destination"]
    progress_label = kwargs["progress_label"]
    progress_title = kwargs["progress_title"]
    progress = kwargs["progress"]
    list_contents = kwargs["list_contents"]
    canvas = kwargs["canvas"]
    sources = kwargs["sources"]

    try:
        # directories
        dest_files = os.listdir(destination)
        # source_files = os.scandir(sources)
        # pages forgotten
        progress_label.place_forget()
        progress_title.place_forget()
        progress.place_forget()
        list_contents.place_forget()
        # frames
        global track_contents, success_content_scrolled_text, unsuccess_content_scrolled_text, table_header
        track_contents = Frame(canvas, width=1030, height=290, bg="white")
        table_header = Frame(track_contents, width=1030, height=25, bg="#ebe9e9")
        # text headers
        Label(table_header, text="Files Successful", bg="#ebe9e9").place(anchor="c", relx=0.25, rely=0.47)
        Label(table_header, text="Files Unsuccessful", bg="#ebe9e9").place(anchor="c", relx=0.7, rely=0.47)
        # canvas borders
        Canvas(track_contents, width=10, height=290).place(anchor="c", relx=0.0129, rely=0.58)
        Canvas(track_contents, width=10, height=290).place(anchor="c", relx=0.5, rely=0.58)
        Canvas(track_contents, width=10, height=290).place(anchor="c", relx=0.994, rely=0.58)
        # inner header
        inner_header = Frame(track_contents, width=485, height=35, bg="white")
        Label(inner_header, text="Name", bg="white").place(anchor="c", relx=0.1, rely=0.5)
        Label(inner_header, text="|", bg="white").place(anchor="c", relx=0.25, rely=0.5)
        Label(inner_header, text="Path", bg="white").place(anchor="c", relx=0.50, rely=0.5)
        Label(inner_header, text="|", bg="white").place(anchor="c", relx=0.74, rely=0.5)
        Label(inner_header, text="Size", bg="white").place(anchor="c", relx=0.88, rely=0.5)
        inner_header.place(anchor="c", relx=0.256, rely=0.19)
        Canvas(inner_header, width=490, height=0.5, bg="black").place(anchor="w", relx=0, rely=0.9)
        # copied inner header
        copy_inner_header = Frame(track_contents, width=490, height=35, bg="white")
        Label(copy_inner_header, text="Name", bg="white").place(anchor="c", relx=0.1, rely=0.5)
        Label(copy_inner_header, text="|", bg="white").place(anchor="c", relx=0.25, rely=0.5)
        Label(copy_inner_header, text="Path", bg="white").place(anchor="c", relx=0.50, rely=0.5)
        Label(copy_inner_header, text="|", bg="white").place(anchor="c", relx=0.74, rely=0.5)
        Label(copy_inner_header, text="Size", bg="white").place(anchor="c", relx=0.88, rely=0.5)
        Canvas(copy_inner_header, width=490, height=0.5, bg="black").place(anchor="w", relx=0, rely=0.9)
        copy_inner_header.place(anchor="c", relx=0.749, rely=0.19)
        # lists
        successful_list = {}
        unsuccessful_list = {}
        # get files
        if len(dest_files) != 0:
            for file in sources:
                if file.split("/")[-1] in os.listdir(destination):
                    successful_list[file.split("/")[-1]] = file
                else:
                    unsuccessful_list[file.split("/")[-1]] = file

        # success scrolled text widget
        success_content_scrolled_text = ScrolledText(track_contents, bg="white", width=58, height=12.2, bd=0)
        success_content_scrolled_text.place(anchor="c", relx=0.255, rely=0.6)
        for file in successful_list.keys():
            lb0 = Label(success_content_scrolled_text, text=f"{file}", bg="white", justify=LEFT,
                        wraplength=70, width=16)
            success_content_scrolled_text.window_create("end", window=lb0)

            lb1 = Label(success_content_scrolled_text, text=f"{successful_list[file]}", bg="white", justify=LEFT,
                        wraplength=200, width=34)
            success_content_scrolled_text.window_create("end", window=lb1)

            file_name = (successful_list[file]).split("/")[-1]
            size_of_file = os.path.getsize(destination + "/" + file_name)

            if size_of_file >= 1000000000:
                size_of_file = str(round((size_of_file / 1000000000), 1)) + " gb"
            elif 1000000 <= size_of_file < 1000000000:
                size_of_file = str(round((size_of_file / 1000000), 1)) + " mb"
            elif size_of_file >= 1000:
                size_of_file = str(round((size_of_file / 1000), 1)) + " kb"
            else:
                size_of_file = str(round(size_of_file, 1)) + " bytes"
            lb2 = Label(success_content_scrolled_text, text=size_of_file, bg="white", justify=LEFT, wraplength=60,
                        width=13)
            success_content_scrolled_text.window_create("end", window=lb2)

            canvas_separator = Canvas(success_content_scrolled_text, width=470, height=5)
            success_content_scrolled_text.window_create("end", window=canvas_separator)

        # unsuccessful scrolled text widget
        unsuccess_content_scrolled_text = ScrolledText(track_contents, bg="white", width=59, height=12.2, bd=0)
        unsuccess_content_scrolled_text.place(anchor="c", relx=0.75, rely=0.6)
        for file in unsuccessful_list.keys():
            lb0 = Label(unsuccess_content_scrolled_text, text=f"{file}", bg="white", justify=LEFT,
                        wraplength=70, width=16)
            success_content_scrolled_text.window_create("end", window=lb0)

            lb1 = Label(unsuccess_content_scrolled_text, text=f"{unsuccessful_list[file]}", bg="white", justify=LEFT,
                        wraplength=200, width=34)
            success_content_scrolled_text.window_create("end", window=lb1)

            file_name = (unsuccessful_list[file]).split("/")[-1]
            size_of_file = os.path.getsize(destination + "/" + file_name)

            if size_of_file >= 1000000000:
                size_of_file = str(round((size_of_file / 1000000000), 1)) + " gb"
            elif 1000000 <= size_of_file < 1000000000:
                size_of_file = str(round((size_of_file / 1000000), 1)) + " mb"
            elif size_of_file >= 1000:
                size_of_file = str(round((size_of_file / 1000), 1)) + " kb"
            else:
                size_of_file = str(round(size_of_file, 1)) + " bytes"

            lb2 = Label(unsuccess_content_scrolled_text, text=size_of_file, bg="white", justify=LEFT, wraplength=60,
                        width=13)
            success_content_scrolled_text.window_create("end", window=lb2)

        table_header.place(anchor="c", relx=0.5, rely=0.1)
        track_contents.place(anchor="c", relx=0.39, rely=0.8)
    except NameError:
        tkinter.messagebox.showinfo("Error Message", "No files copied")
    return 0


#       end of files tracker
#       start of folders tracker


def track_folder(**kwargs):
    destination = kwargs["destination"]
    progress_label = kwargs["progress_label"]
    progress_title = kwargs["progress_title"]
    progress = kwargs["progress"]
    list_contents = kwargs["list_contents"]
    canvas = kwargs["canvas"]
    sources = kwargs["sources"]


    try:
        # directories
        dest_files = os.listdir(destination)
        source_files = os.scandir(sources)
        # pages forgotten
        progress_label.place_forget()
        progress_title.place_forget()
        progress.place_forget()
        list_contents.place_forget()
        # frames
        global track_contents, success_content_scrolled_text, unsuccess_content_scrolled_text, table_header
        track_contents = Frame(canvas, width=1030, height=290, bg="white")
        table_header = Frame(track_contents, width=1030, height=25, bg="#ebe9e9")
        # text headers
        Label(table_header, text="Files Successful", bg="#ebe9e9").place(anchor="c", relx=0.25, rely=0.47)
        Label(table_header, text="Files Unsuccessful", bg="#ebe9e9").place(anchor="c", relx=0.7, rely=0.47)
        # canvas borders
        Canvas(track_contents, width=10, height=290).place(anchor="c", relx=0.0129, rely=0.58)
        Canvas(track_contents, width=10, height=290).place(anchor="c", relx=0.5, rely=0.58)
        Canvas(track_contents, width=10, height=290).place(anchor="c", relx=0.994, rely=0.58)
        # inner header
        inner_header = Frame(track_contents, width=485, height=35, bg="white")
        Label(inner_header, text="Name", bg="white").place(anchor="c", relx=0.1, rely=0.5)
        Label(inner_header, text="|", bg="white").place(anchor="c", relx=0.25, rely=0.5)
        Label(inner_header, text="Path", bg="white").place(anchor="c", relx=0.50, rely=0.5)
        Label(inner_header, text="|", bg="white").place(anchor="c", relx=0.74, rely=0.5)
        Label(inner_header, text="Size", bg="white").place(anchor="c", relx=0.88, rely=0.5)
        inner_header.place(anchor="c", relx=0.256, rely=0.19)
        Canvas(inner_header, width=490, height=0.5, bg="black").place(anchor="w", relx=0, rely=0.9)
        # copied inner header
        copy_inner_header = Frame(track_contents, width=490, height=35, bg="white")
        Label(copy_inner_header, text="Name", bg="white").place(anchor="c", relx=0.1, rely=0.5)
        Label(copy_inner_header, text="|", bg="white").place(anchor="c", relx=0.25, rely=0.5)
        Label(copy_inner_header, text="Path", bg="white").place(anchor="c", relx=0.50, rely=0.5)
        Label(copy_inner_header, text="|", bg="white").place(anchor="c", relx=0.74, rely=0.5)
        Label(copy_inner_header, text="Size", bg="white").place(anchor="c", relx=0.88, rely=0.5)
        Canvas(copy_inner_header, width=490, height=0.5, bg="black").place(anchor="w", relx=0, rely=0.9)
        copy_inner_header.place(anchor="c", relx=0.749, rely=0.19)
        # lists
        successful_list = {}
        unsuccessful_list = {}
        # get files
        if sources.split("/")[-1] in dest_files:
            for file in source_files:
                if file.name in os.listdir(destination + "/" + sources.split("/")[-1]):
                    successful_list[file.name] = file.path
                else:
                    unsuccessful_list[file.name] = file.path

        # success scrolled text widget
        success_content_scrolled_text = ScrolledText(track_contents, bg="white", width=58, height=12.2, bd=0)
        success_content_scrolled_text.place(anchor="c", relx=0.255, rely=0.6)
        for file in successful_list.keys():
            lb0 = Label(success_content_scrolled_text, text=f"{file}", bg="white", justify=LEFT,
                        wraplength=70, width=16)
            success_content_scrolled_text.window_create("end", window=lb0)

            # split file path
            successful_list_splitted = str(successful_list[file]).split("\\")
            reformatted_path = '/'.join(successful_list_splitted)

            lb1 = Label(success_content_scrolled_text, text=f"{reformatted_path}", bg="white", justify=LEFT,
                        wraplength=200, width=34)
            success_content_scrolled_text.window_create("end", window=lb1)

            file_name = (reformatted_path).split("/")[-1]
            size_of_file = os.path.getsize(destination + "/" + file_name)

            if size_of_file >= 1000000000:
                size_of_file = str(size_of_file / 1000000000) + " gb"
            elif 1000000 <= size_of_file < 1000000000:
                size_of_file = str(size_of_file / 1000000) + " mb"
            elif size_of_file >= 1000:
                size_of_file = str(size_of_file / 1000) + " kb"
            else:
                size_of_file = str(size_of_file) + " bytes"
            lb2 = Label(success_content_scrolled_text, text=size_of_file, bg="white", justify=LEFT, wraplength=60,
                        width=13)
            success_content_scrolled_text.window_create("end", window=lb2)

            canvas_separator = Canvas(success_content_scrolled_text, width=470, height=5)
            success_content_scrolled_text.window_create("end", window=canvas_separator)

        # unsuccessful scrolled text widget
        unsuccess_content_scrolled_text = ScrolledText(track_contents, bg="white", width=59, height=12.2, bd=0)
        unsuccess_content_scrolled_text.place(anchor="c", relx=0.75, rely=0.6)
        for file in unsuccessful_list.keys():
            lb0 = Label(unsuccess_content_scrolled_text, text=f"{file}", bg="white", justify=LEFT,
                        wraplength=70, width=16)
            success_content_scrolled_text.window_create("end", window=lb0)

            # split file path
            successful_list_splitted = str(successful_list[file]).split("\\")
            reformatted_path = '/'.join(successful_list_splitted)

            lb1 = Label(unsuccess_content_scrolled_text, text=f"{reformatted_path}", bg="white", justify=LEFT,
                        wraplength=200, width=34)
            success_content_scrolled_text.window_create("end", window=lb1)

            file_name = (reformatted_path).split("/")[-1]
            size_of_file = os.path.getsize(destination + "/" + file_name)

            if size_of_file >= 1000000000:
                size_of_file = str(size_of_file / 1000000000) + " gb"
            elif 1000000 <= size_of_file < 1000000000:
                size_of_file = str(size_of_file / 1000000) + " mb"
            elif size_of_file >= 1000:
                size_of_file = str(size_of_file / 1000) + " kb"
            else:
                size_of_file = str(size_of_file) + " bytes"

            lb2 = Label(unsuccess_content_scrolled_text, text=size_of_file, bg="white", justify=LEFT, wraplength=60,
                        width=13)
            success_content_scrolled_text.window_create("end", window=lb2)

        table_header.place(anchor="c", relx=0.5, rely=0.1)
        track_contents.place(anchor="c", relx=0.39, rely=0.8)
    except NameError:
        tkinter.messagebox.showinfo("Error Message", "No files copied")
    return 0


#       end of folders tracker
#   end of trackers