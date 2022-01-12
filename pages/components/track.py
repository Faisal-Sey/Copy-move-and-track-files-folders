from . import progress_bar as pb, copyer

def tracker(copied, total_files):
    from . import utils
    global size_obtained
    print(total_files)
    if total_files == 1:
        if int(copied) < 1e3:
            current_size = str(round(int(copied), 1)) + " bytes"
        elif 1e3 <= int(copied) < 1e6:
            current_size = str(round((int(copied) / 1E3), 1)) + " KB"
        elif 1e6 <= int(copied) < 1e9:
            current_size = str(round((int(copied) / 1E6), 1)) + " MB"
        else:
            current_size = str(round((int(copied) / 1E9), 1)) + " GB"

        pb.bars_files(
            current_size=current_size,
            copied=copied,
            total_files=total_files,
            file_sizes=copyer.file_sizes,
            copy_file_sizes=copyer.copy_file_sizes,
            my_copy_file=utils.my_copy_file,
            files_total=copyer.files_total,
            FILE_SIZE=copyer.FILE_SIZE,
            total_size=copyer.total_size,
            progress_label = copyer.progress_label,
            progress=copyer.progress,
            percentage=copyer.percentage,
            app=copyer.app
        )
    else:
        current_size = ''
        size_obtained = utils.size_obtained + copied
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
    from . import utils
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

        pb.bars_folder(
            current_size=current_size,
            copied=copied,
            total_files=total_files,
            file_sizes=copyer.file_sizes,
            copy_file_sizes=copyer.copy_file_sizes,
            my_copy_file=utils.my_copy_file,
            files_total=copyer.files_total,
            FILE_SIZE=copyer.FILE_SIZE,
            total_size=copyer.total_size,
            progress_label = copyer.progress_label,
            progress=copyer.progress,
            percentage=copyer.percentage,
            app=copyer.app
        )
    else:
        current_size = ''
        size_obtained = utils.size_obtained + copied
        if int(size_obtained) < 1e3:
            current_size = str(round(int(size_obtained), 1)) + " bytes"
        elif 1e3 <= int(size_obtained) < 1e6:
            current_size = str(round((int(size_obtained) / 1E3), 1)) + " KB"
        elif 1e6 <= int(size_obtained) < 1e9:
            current_size = str(round(int(size_obtained) / 1E6, 1)) + " MB"
        else:
            current_size = str(round(int(size_obtained) / 1E9, 1)) + " GB"

        pb.bars_folder(
            current_size=current_size,
            copied=copied,
            total_files=total_files,
            file_sizes=copyer.file_sizes,
            copy_file_sizes=copyer.copy_file_sizes,
            my_copy_folder=utils.my_copy_folder,
            files_total=copyer.files_total,
            FILE_SIZE=copyer.FILE_SIZE,
            total_size=copyer.total_size,
            progress_label = copyer.progress_label,
            progress=copyer.progress,
            percentage=copyer.percentage,
            app=copyer.app
        )

