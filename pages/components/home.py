from tkinter import *
from . import transfer, utils

# home page


def homepage(app):

    # top menu frame
    top_menu_frame = Frame(app, width=1920, height=60)

    # file menu button
    file_menu_btn = Menubutton(top_menu_frame, text="File", relief=RAISED, bd=0,
                               activeforeground="white", activebackground="blue")
    # file menu
    file_menu = Menu(file_menu_btn, tearoff=0)
    file_menu_btn["menu"] = file_menu
    file_menu.add_command(label="New")
    file_menu.add_command(label="Save")
    file_menu.add_command(label="Save As")
    file_menu.add_command(label="Exit")
    file_menu_btn.place(anchor="c", relx=0.01, rely=0.745)

    # edit menu button
    edit_menu_btn = Menubutton(top_menu_frame, text="Edit", relief=RAISED, bd=0,
                               activeforeground="white", activebackground="blue")
    edit_menu_btn.place(anchor="c", relx=0.026, rely=0.745)
    # edit menu
    edit_menu = Menu(edit_menu_btn, tearoff=0)
    edit_menu_btn["menu"] = edit_menu
    edit_menu.add_command(label="Find")
    edit_menu.add_command(label="Replace")

    # view menu button
    view_menu_btn = Menubutton(top_menu_frame, text="View", relief=RAISED, bd=0,
                               activeforeground="white", activebackground="blue")
    # view menu
    view_menu = Menu(view_menu_btn, tearoff=0)
    view_menu_btn["menu"] = view_menu
    view_menu.add_command(label="Themes")
    view_menu.add_command(label="Preferences")
    view_menu_btn.place(anchor="c", relx=0.044, rely=0.745)

    # help menu button
    help_menu_btn = Menubutton(top_menu_frame, text="Help", relief=RAISED, bd=0,
                               activeforeground="white", activebackground="blue")
    # help menu
    help_menu = Menu(help_menu_btn, tearoff=0)
    help_menu_btn["menu"] = help_menu
    help_menu.add_command(label="About")
    help_menu.add_command(label="Update")
    help_menu_btn.place(anchor="c", relx=0.063, rely=0.745)

    top_menu_frame.place(anchor="w", relx=0, rely=0)

    # canvas separator
    canvas = Canvas(app, width=1920, height=0.5, bg="#d0cece")
    canvas.create_line(50, 50, 100, 100)
    canvas.place(anchor="w", relx=0, rely=0.035)

    # Tutorials label
    tuts_label = Button(app, text="Tutorials", bd=0)
    tuts_label.place(anchor="c", relx=0.02, rely=0.05)

    # Vertical label
    vertical_label = Button(app, text="     |     ", bd=0)
    vertical_label.place(anchor="c", relx=0.05, rely=0.05)

    # Docs label
    docs_label = Button(app, text="Docs", bd=0)
    docs_label.place(anchor="c", relx=0.07, rely=0.05)

    # canvas separator
    canvas = Canvas(app, width=1920, height=0.5, bg="#d0cece")
    canvas.create_line(50, 50, 100, 100)
    canvas.place(anchor="w", relx=0, rely=0.065)

    # canvas title
    canvas = Canvas(app, width=1220, height=55, bg="#ffffff")
    Label(canvas, text="COPY AND TRACK FILES VERSION 1.0", fg="blue", bg="white").place(
        anchor="c", relx=0.5, rely=0.5)
    canvas.place(anchor="w", relx=0.1, rely=0.12)

    # canvas body
    canvas = Canvas(app, width=1300, height=650, bg="#ffffff")

    Label(canvas, bg="white", text="Copy and Track Folders and Files from one location "
                                   "to another location").place(anchor="c",
                                                                relx=0.5,
                                                                rely=0.05)
    Label(canvas, bg="white", image=utils.folder_image).place(anchor="c", relx=0.36, rely=0.25)
    Label(canvas, bg="white", image=utils.forward_image).place(anchor="c", relx=0.50, rely=0.25)
    Label(canvas, bg="white", image=utils.folder_image).place(anchor="c", relx=0.63, rely=0.25)
    Button(canvas, text="Transfer & Track Folders", width=50, height=3, bg="white",
           command=lambda: transfer.directory_transfer(
               app=app
           ), bd=3).place(anchor="c", relx=0.5, rely=0.45)
    Label(canvas, bg="white", image=utils.file_image).place(anchor="c", relx=0.36, rely=0.65)
    Label(canvas, bg="white", image=utils.forward_image).place(anchor="c", relx=0.50, rely=0.65)
    Label(canvas, bg="white", image=utils.folder_image).place(anchor="c", relx=0.63, rely=0.65)
    Button(canvas, text="Transfer & Track Files", width=50, height=3, bg="white", command=lambda: transfer.file_transfer(
        app=app
    ),
           bd=3).place(anchor="c", relx=0.5, rely=0.85)
    canvas.place(anchor="w", relx=0.07, rely=0.55)


# --- app content ends --- #