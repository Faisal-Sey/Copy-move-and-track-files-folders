import tkinter

#       add text to file text entry

def add_text_to_source(*args, **kwargs):
    sources = kwargs["sources"]
    src_text_widget = kwargs["src_text_widget"]
    folder_source_is_not_empty = kwargs["folder_source_is_not_empty"]
    try:
        if sources == "":
            tkinter.messagebox.showinfo("Error Message", "No source directory specified")
        else:
            src_text_widget.delete("0.0", "insert")
            src_text_widget.insert("insert", sources)
        folder_source_is_not_empty = True
    except NameError:
        tkinter.messagebox.showinfo("Error Message", "No source directory specified")


def add_filenames_to_text(*args, **kwargs):
    sources = kwargs["sources"]
    src_text_widget = kwargs["src_text_widget"]
    file_source_is_not_empty = kwargs["folder_source_is_not_empty"]
    
    try:
        if sources == ():
            tkinter.messagebox.showinfo("Error Message", "No source directory specified")
        else:
            for files in sources:
                file_name = files.split("/")[-1]
                src_text_widget.insert("insert", file_name)
                if sources[-1] == files:
                    pass
                else:
                    src_text_widget.insert("insert", ", ")
        file_source_is_not_empty = True
    except NameError:
        tkinter.messagebox.showinfo("Error Message", "No source directory specified")


#       add text to destination text entry


def add_text_to_dest(*args, **kwargs):
    destination = kwargs["destination"]
    dest_text_widget = kwargs["dest_text_widget"]

    try:
        if destination == "":
            tkinter.messagebox.showinfo("Error Message", "No destination directory specified")
        else:
            dest_text_widget.delete("0.0", "insert")
            dest_text_widget.insert("insert", destination)
        destination_is_not_empty = True
    except NameError:
        tkinter.messagebox.showinfo("Error Message", "No destination directory specified")


#   end insert of text functions

