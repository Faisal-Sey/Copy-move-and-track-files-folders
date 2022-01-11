from tkinter import filedialog
import add_text

def get_files_from_folder(src_or_dest):
    global sources, destination
    if src_or_dest == "src":
        file_names = filedialog.askdirectory()
        sources = file_names
        add_text.add_text_to_source()
    elif src_or_dest == "dest":
        file_names = filedialog.askdirectory()
        destination = file_names
        add_text.add_text_to_dest()


#       get files


def get_files(src_or_dest):
    global sources, destination
    if src_or_dest == "src":
        file_names = filedialog.askopenfilenames()
        sources = file_names
        add_text.add_filenames_to_text()

    elif src_or_dest == "dest":
        file_names = filedialog.askdirectory()
        destination = file_names
        add_text.add_text_to_dest()
