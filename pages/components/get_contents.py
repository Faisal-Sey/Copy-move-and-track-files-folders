from tkinter import filedialog
from . import add_text

def get_files_from_folder(**kwargs):
    src_or_dest = kwargs["src_or_dest"]
    src_text_widget = kwargs["src_text_widget"]
    dest_text_widget = kwargs["dest_text_widget"]

    if src_or_dest == "src":
        file_names = filedialog.askdirectory()
        sources = file_names
        add_text.add_text_to_source(
            sources=sources,
            src_text_widget=src_text_widget
        )
    elif src_or_dest == "dest":
        file_names = filedialog.askdirectory()
        destination = file_names
        add_text.add_text_to_dest(
            destination=destination,
            dest_text_widget=dest_text_widget
        )


#       get files


def get_files(**kwargs):
    src_or_dest = kwargs["src_or_dest"]
    src_text_widget = kwargs["src_text_widget"]
    dest_text_widget = kwargs["dest_text_widget"]
    
    if src_or_dest == "src":
        file_names = filedialog.askopenfilenames()
        sources = file_names
        add_text.add_filenames_to_text(
            sources=sources,
            src_text_widget=src_text_widget
        )

    elif src_or_dest == "dest":
        file_names = filedialog.askdirectory()
        destination = file_names
        add_text.add_text_to_dest(
            destination=destination,
            dest_text_widget=dest_text_widget
        )
