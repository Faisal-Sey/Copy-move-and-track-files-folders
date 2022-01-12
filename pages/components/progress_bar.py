from tkinter import *

def bars_files(**kwargs):
    #   start of progress bar handler
    done = PhotoImage(file="../../src/done_1.png").subsample(8, 8)
    current_size = kwargs["current_size"] 
    copied = kwargs["copied"] 
    total_files = kwargs["total_files"] 
    file_sizes = kwargs["file_sizes"] 
    copy_file_sizes = kwargs["copy_file_sizes"] 
    my_copy_file = kwargs["my_copy_file"] 
    files_total = kwargs["files_total"] 
    FILE_SIZE = kwargs["FILE_SIZE"] 
    total_size = kwargs["total_size"] 
    progress_label = kwargs["progress_label"] 
    progress = kwargs["progress"] 
    percentage = kwargs["percentage"] 
    app = kwargs["app"] 


    total = total_files
    current_i = 0
    i = 0
    if int(copied) >= file_sizes[0]:
        item = file_sizes.pop(0)
        current_i = copy_file_sizes.index(item)
        i = copy_file_sizes.index(item) + 1

    current_percent = 0
    try:
        if total > 1:
            my_copy_file = my_copy_file + (copied * (100 / copy_file_sizes[current_i]))
            total_percent = 100 * total
            current_percent = (my_copy_file / total_percent) * 100
        else:
            new_copy = copied * (100 / copy_file_sizes[current_i])
            total_percent = 100 * total
            current_percent = (new_copy / total_percent) * 100
    except IndexError:
        pass

    files_total["text"] = "Total Files: " + str(i) + "/" + str(total)
    if int(FILE_SIZE) < 1E3:
        file_size_string = str(round(FILE_SIZE, 1)) + " bytes"
    elif 1E3 <= int(FILE_SIZE) < 1E6:
        file_size_string = str(round((FILE_SIZE / 1E3), 1)) + " KB"
    elif 1E6 <= int(FILE_SIZE) < 1E9:
        file_size_string = str(round((FILE_SIZE / 1E6), 1)) + " MB"
    else:
        file_size_string = str(round((FILE_SIZE / 1E9), 1)) + " GB"

    total_size["text"] = "Total Size: " + str(current_size) + "/" + str(file_size_string)
    percentage["text"] = "Percentages: " + str(round(current_percent)) + "/" + "100"
    if round(current_percent) == 100:
        progress_label["image"] = done
        app.update_idletasks()
    progress["value"] = current_percent
    app.update_idletasks()


def bars_folder(**kwargs):
    #   start of progress bar handler
    done = PhotoImage(file="../../src/done_1.png").subsample(8, 8)
    current_size = kwargs["current_size"] 
    copied = kwargs["copied"] 
    total_files = kwargs["total_files"] 
    file_sizes = kwargs["file_sizes"] 
    copy_file_sizes = kwargs["copy_file_sizes"] 
    my_copy_folder = kwargs["my_copy_folder"] 
    files_total = kwargs["files_total"] 
    FILE_SIZE = kwargs["FILE_SIZE"] 
    total_size = kwargs["total_size"] 
    progress_label = kwargs["progress_label"] 
    progress = kwargs["progress"] 
    percentage = kwargs["percentage"] 
    app = kwargs["app"] 

    total = total_files
    current_i = 0
    i = 0
    if int(copied) >= file_sizes[0]:
        item = file_sizes.pop(0)
        current_i = copy_file_sizes.index(item)
        i = copy_file_sizes.index(item) + 1

    current_percent = 0
    try:
        if total > 1:
            my_copy_folder = my_copy_folder + (copied * (100 / copy_file_sizes[current_i]))
            total_percent = 100 * total
            current_percent = (my_copy_folder / total_percent) * 100
        else:
            new_copy = copied * (100 / copy_file_sizes[current_i])
            total_percent = 100 * total
            current_percent = (new_copy / total_percent) * 100
    except IndexError:
        pass

    files_total["text"] = "Total Files: " + str(i) + "/" + str(total)
    if int(FILE_SIZE) < 1E3:
        file_size_string = str(round(FILE_SIZE, 1)) + " bytes"
    elif 1E3 <= int(FILE_SIZE) < 1E6:
        file_size_string = str(round((FILE_SIZE / 1E3), 1)) + " KB"
    elif 1E6 <= int(FILE_SIZE) < 1E9:
        file_size_string = str(round((FILE_SIZE / 1E6), 1)) + " MB"
    else:
        file_size_string = str(round((FILE_SIZE / 1E9), 1)) + " GB"

    total_size["text"] = "Total Size: " + str(current_size) + "/" + str(file_size_string)
    percentage["text"] = "Percentages: " + str(round(current_percent)) + "/" + "100"
    if round(current_percent) == 100:
        progress_label["image"] = done
        app.update_idletasks()
    progress["value"] = current_percent
    app.update_idletasks()


#   end of progress bar handler