import os

foldername = "misc"
if foldername:
    try:
        os.makedirs(foldername)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise