from tkinter import *

# loading pics

folder_image = PhotoImage(file="./src/folder.png").subsample(3, 3)
file_image = PhotoImage(file="./src/file.png").subsample(3, 3)
forward_image = PhotoImage(file="./src/forward.png").subsample(10, 10)
progress_image = PhotoImage(file="./src/progress_1.png").subsample(8, 8)
done = PhotoImage(file="./src/done_1.png").subsample(8, 8)


# boolean vars
file_source_is_not_empty = False
folder_source_is_not_empty = False
destination_is_not_empty = False

# other vars
size_obtained = 0
my_copy_file = 0
my_copy_folder = 0