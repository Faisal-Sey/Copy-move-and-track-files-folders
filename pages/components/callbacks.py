from . import track, copyer


def callback_function(copied):
    track.tracker(copied)


def callback_function_folder(copied):
    track.tracker_folder(copied, copyer.total_files)