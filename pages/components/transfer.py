from tkinter import *
from . import copyer, move, trackers, utils, get_contents
from tkinter.ttk import Progressbar

# file transfer page


def file_transfer(**kwargs):
    app = kwargs["app"]

    # canvas body
    canvas = Canvas(app, width=1300, height=650, bg="#ffffff")

    # frame body
    canvas_body_frame = Frame(canvas, width=300, height=1350, bg="#d0cece")
    canvas_body_frame.place(anchor="c", relx=0.9, rely=0)

    Button(canvas_body_frame, text="COPY", width=30, height=3, bg="white", command=copyer.copy_files).place(anchor="c",
                                                                                                     relx=0.5,
                                                                                                     rely=0.6)
    Button(canvas_body_frame, text="MOVE", width=30, height=3, bg="white", command=move.move_files).place(anchor="c",
                                                                                                     relx=0.5,
                                                                                                     rely=0.65)
    Button(canvas_body_frame, text="TRACK", width=30, height=3, bg="white", command=trackers.track_files).place(anchor="c",
                                                                                                       relx=0.5,
                                                                                                       rely=0.7)
    Button(canvas_body_frame, text="Copy Folders instead", width=30, height=3, bg="white",
           command=directory_transfer).place(anchor="c", relx=0.5, rely=0.9)
    Label(canvas, bg="white", text="Copy and Track files from one location "
                                   "to another location").place(anchor="c",
                                                                relx=0.4,
                                                                rely=0.05)
    Label(canvas, bg="white", image=utils.file_image).place(anchor="c", relx=0.26, rely=0.25)
    Label(canvas, bg="white", image=utils.forward_image).place(anchor="c", relx=0.40, rely=0.25)
    Label(canvas, bg="white", image=utils.folder_image).place(anchor="c", relx=0.53, rely=0.25)
    scrollbar_src = Scrollbar(canvas)
    scrollbar_src.place(anchor="c", relx=0.35, rely=0.41, height=70)
    src_text_widget = Text(canvas, bd=5, height=4, width=25, yscrollcommand=scrollbar_src.set)
    scrollbar_src.config(command=src_text_widget.yview)
    src_text_widget.place(anchor="c", relx=0.26, rely=0.41)
    scrollbar_dest = Scrollbar(canvas)
    scrollbar_dest.place(anchor="c", relx=0.62, rely=0.41, height=70)
    dest_text_widget = Text(canvas, bd=5, height=4, width=25, yscrollcommand=scrollbar_dest.set)
    dest_text_widget.place(anchor="c", relx=0.53, rely=0.41)
    scrollbar_dest.config(command=dest_text_widget.yview)
    Button(canvas, text="Open Source directory", command=lambda: get_contents.get_files("src")).place(anchor="c", relx=0.26,
                                                                                         rely=0.5)
    Button(canvas, text="Open Destination directory", command=lambda: get_contents.get_files("dest")).place(anchor="c", relx=0.53,
                                                                                               rely=0.5)
    list_contents = Frame(canvas, width=1030, height=290, bg="#ebe9e9")
    progress_label = Label(list_contents, image=utils.progress_image)
    progress_label.place(anchor="c", relx=0.5, rely=0.2)
    progress = Progressbar(list_contents, orient=HORIZONTAL, length=100,
                           mode='determinate')

    progress.place(anchor="c", relx=0.5, rely=0.5, width=150, height=30)
    files_total = Label(list_contents, text="Total Files: 0/0", bg="#ebe9e9")
    files_total.place(anchor="c", relx=0.5, rely=0.65)
    total_size = Label(list_contents, text="Total Size: 0/0", bg="#ebe9e9")
    total_size.place(anchor="c", relx=0.5, rely=0.74)
    percentage = Label(list_contents, text="Percentage: 0/100", bg="#ebe9e9")
    percentage.place(anchor="c", relx=0.5, rely=0.83)
    list_contents.place(anchor="c", relx=0.39, rely=0.8)
    progress_title = Label(app, text="Progress Bar", bg="white")
    progress_title.place(anchor="c", relx=0.10, rely=0.598)
    canvas.place(anchor="w", relx=0.07, rely=0.55)

    # copyright label
    copyright_label = Label(app, text="Copyright 2021")
    copyright_label.place(anchor="c", relx=0.5, rely=0.97)


# folder transfer page


def directory_transfer(**kwargs):
    app = kwargs["app"]

    # canvas body
    canvas = Canvas(app, width=1300, height=650, bg="#ffffff")

    # frame body
    canvas_body_frame = Frame(canvas, width=300, height=1350, bg="#d0cece")
    canvas_body_frame.place(anchor="c", relx=0.9, rely=0)

    Button(canvas_body_frame, text="COPY", width=30, height=3, bg="white", command=copyer.copy_folders).place(anchor="c",
                                                                                                       relx=0.5,
                                                                                                       rely=0.6)
    Button(canvas_body_frame, text="MOVE", width=30, height=3, bg="white", command=move.move_folder).place(anchor="c",
                                                                                                        relx=0.5,
                                                                                                        rely=0.65)
    Button(canvas_body_frame, text="TRACK", width=30, height=3, bg="white", command=trackers.trackers.track_folder).place(anchor="c",
                                                                                                        relx=0.5,
                                                                                                        rely=0.7)
    Button(canvas_body_frame, text="Copy Files instead", width=30, height=3, bg="white",
           command=file_transfer).place(anchor="c", relx=0.5, rely=0.9)
    Label(canvas, bg="white", text="Copy and Track files from one location "
                                   "to another location").place(anchor="c",
                                                                relx=0.4,
                                                                rely=0.05)
    Label(canvas, bg="white", image=utils.folder_image).place(anchor="c", relx=0.26, rely=0.25)
    Label(canvas, bg="white", image=utils.forward_image).place(anchor="c", relx=0.40, rely=0.25)
    Label(canvas, bg="white", image=utils.folder_image).place(anchor="c", relx=0.53, rely=0.25)
    scrollbar_src = Scrollbar(canvas)
    scrollbar_src.place(anchor="c", relx=0.35, rely=0.41, height=70)
    src_text_widget = Text(canvas, bd=5, height=4, width=25, yscrollcommand=scrollbar_src.set)
    scrollbar_src.config(command=src_text_widget.yview)
    src_text_widget.place(anchor="c", relx=0.26, rely=0.41)
    scrollbar_dest = Scrollbar(canvas)
    scrollbar_dest.place(anchor="c", relx=0.62, rely=0.41, height=70)
    dest_text_widget = Text(canvas, bd=5, height=4, width=25, yscrollcommand=scrollbar_dest.set)
    dest_text_widget.place(anchor="c", relx=0.53, rely=0.41)
    scrollbar_dest.config(command=dest_text_widget.yview)
    Button(canvas, text="Open Source directory", command=lambda: get_contents.get_files_from_folder("src")).place(anchor="c",
                                                                                                     relx=0.26,
                                                                                                     rely=0.5)
    Button(canvas, text="Open Destination directory", command=lambda: get_contents.get_files_from_folder("dest")).place(anchor="c",
                                                                                                           relx=0.53,
                                                                                                           rely=0.5)
    list_contents = Frame(canvas, width=1030, height=290, bg="#ebe9e9")
    progress_label = Label(list_contents, image=utils.progress_image)
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
    canvas.place(anchor="w", relx=0.07, rely=0.55)

    # copyright label
    copyright_label = Label(app, text="Copyright 2021")
    copyright_label.place(anchor="c", relx=0.5, rely=0.97)
