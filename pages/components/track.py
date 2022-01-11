import progress_bar as pb


def tracker(copied, total_files):
    global size_obtained
    if total_files == 1:
        if int(copied) < 1e3:
            current_size = str(round(int(copied), 1)) + " bytes"
        elif 1e3 <= int(copied) < 1e6:
            current_size = str(round((int(copied) / 1E3), 1)) + " KB"
        elif 1e6 <= int(copied) < 1e9:
            current_size = str(round((int(copied) / 1E6), 1)) + " MB"
        else:
            current_size = str(round((int(copied) / 1E9), 1)) + " GB"

        pb.bars_files(current_size, copied)
    else:
        current_size = ''
        size_obtained = size_obtained + copied
        if int(size_obtained) < 1e3:
            current_size = str(round(int(size_obtained), 1)) + " bytes"
        elif 1e3 <= int(size_obtained) < 1e6:
            current_size = str(round((int(size_obtained) / 1E3), 1)) + " KB"
        elif 1e6 <= int(size_obtained) < 1e9:
            current_size = str(round(int(size_obtained) / 1E6, 1)) + " MB"
        else:
            current_size = str(round(int(size_obtained) / 1E9, 1)) + " GB"

        pb.bars_files(current_size, copied)


def tracker_folder(copied, total_files):
    global size_obtained
    if total_files == 1:
        if int(copied) < 1e3:
            current_size = str(round(int(copied), 1)) + " bytes"
        elif 1e3 <= int(copied) < 1e6:
            current_size = str(round((int(copied) / 1E3), 1)) + " KB"
        elif 1e6 <= int(copied) < 1e9:
            current_size = str(round((int(copied) / 1E6), 1)) + " MB"
        else:
            current_size = str(round((int(copied) / 1E9), 1)) + " GB"

        pb.bars_folder(current_size, copied)
    else:
        current_size = ''
        size_obtained = size_obtained + copied
        if int(size_obtained) < 1e3:
            current_size = str(round(int(size_obtained), 1)) + " bytes"
        elif 1e3 <= int(size_obtained) < 1e6:
            current_size = str(round((int(size_obtained) / 1E3), 1)) + " KB"
        elif 1e6 <= int(size_obtained) < 1e9:
            current_size = str(round(int(size_obtained) / 1E6, 1)) + " MB"
        else:
            current_size = str(round(int(size_obtained) / 1E9, 1)) + " GB"

        pb.bars_folder(current_size, copied)

